// Headless screenshot harness (Chrome DevTools Protocol, no dependencies).
// usage: node tools/shot.js <url> <outprefix> <t1,t2,...seconds> [width height] [js-to-eval-before-shots]
// GPU-backed by default (fine for canvas/WebGL on a Mac).
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const [,, url, prefix, timesArg, W = '1280', H = '720', pre = ''] = process.argv;
const times = timesArg.split(',').map(Number);
const port = 9222 + Math.floor(Math.random() * 500);
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', '--ignore-gpu-blocklist', '--hide-scrollbars', '--no-first-run',
   '--user-data-dir=/tmp/shot-profile-' + port, '--remote-debugging-port=' + port,
   `--window-size=${W},${H}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
function getJSON(p) { return new Promise((res, rej) => http.get(`http://127.0.0.1:${port}${p}`, r => { let d=''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d))); }).on('error', rej)); }
(async () => {
  let targets;
  for (let i = 0; i < 50; i++) { try { targets = await getJSON('/json'); break; } catch (e) { await sleep(200); } }
  const page = targets.find(t => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  let id = 0; const pending = {}; const logs = [];
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending[m.id]) { pending[m.id](m); delete pending[m.id]; }
    if (m.method === 'Runtime.exceptionThrown') logs.push('EXC ' + JSON.stringify(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text));
    if (m.method === 'Runtime.consoleAPICalled' && (m.params.type === 'error' || m.params.type === 'warning')) logs.push(m.params.type + ' ' + m.params.args.map(a => a.value || a.description).join(' ')); };
  const send = (method, params = {}) => new Promise(r => { const i = ++id; pending[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
  await send('Runtime.enable'); await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 1, mobile: false });
  await send('Page.navigate', { url });
  const t0 = Date.now();
  let preDone = false;
  for (const t of times) {
    const wait = t0 + t * 1000 - Date.now(); if (wait > 0) await sleep(wait);
    if (pre && !preDone) { preDone = true; await send('Runtime.evaluate', { expression: pre, awaitPromise: true }); await sleep(600); }
    const r = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${prefix}_${t}s.png`, Buffer.from(r.result.data, 'base64'));
  }
  const fps = await send('Runtime.evaluate', { expression: `new Promise(r=>{let n=0,t=performance.now();function f(){n++; if(performance.now()-t>1000) r(n); else requestAnimationFrame(f)} requestAnimationFrame(f)})`, awaitPromise: true });
  console.log('fps ~', fps.result.result.value);
  console.log(logs.length ? logs.join('\n') : 'no console errors');
  ws.close(); chrome.kill();
  try { fs.rmSync('/tmp/shot-profile-' + port, { recursive: true, force: true }); } catch (e) {}
})().catch(e => { console.error(e); chrome.kill(); process.exit(1); });
