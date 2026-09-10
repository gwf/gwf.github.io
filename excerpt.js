// In-page excerpt reader.  Shows the rendered pages of one short excerpt
// (see data/excerpts.json) in a lightbox; no PDF is ever linked.
// Usage: CBNExcerpt.open("ch8", "../") — second argument is the path to
// the repo root from the current page.
var CBNExcerpt = (function() {
  var list = null, root = "", box = null;
  function load(cb) {
    if (list) return cb(list);
    var x = new XMLHttpRequest(); x.open("GET", root + "data/excerpts.json");
    x.onload = function() { try { list = JSON.parse(x.responseText).excerpts; } catch (e) { list = []; } cb(list); };
    x.onerror = function() { cb([]); }; x.send();
  }
  function ensure() {
    if (box) return box;
    var css = document.createElement("style");
    css.textContent = "#cbnx{position:fixed;inset:0;background:rgba(0,0,0,.82);z-index:1000;display:flex;flex-direction:column;align-items:center;overflow-y:auto;padding:54px 12px 40px}" +
      "#cbnx .bar{position:fixed;top:0;left:0;right:0;height:44px;background:rgba(12,12,14,.96);border-bottom:1px solid #2a2a2e;display:flex;align-items:center;gap:16px;padding:0 16px;color:#ddd;font:14px -apple-system,Helvetica,Arial,sans-serif}" +
      "#cbnx .bar b{font:400 15px Georgia,serif;color:#f2f2f2}#cbnx .bar span{color:#8a8f99}#cbnx .bar button{margin-left:auto;background:none;border:0;color:#aaa;font-size:24px;cursor:pointer}" +
      "#cbnx img{max-width:min(96vw,820px);width:100%;background:#fff;box-shadow:0 2px 20px rgba(0,0,0,.7);margin-bottom:14px;display:block}" +
      "#cbnx .note{color:#8a8f99;font:13px -apple-system,Helvetica,Arial,sans-serif;max-width:820px;text-align:center;margin:6px 0 18px}";
    document.head.appendChild(css);
    box = document.createElement("div"); box.id = "cbnx"; box.style.display = "none";
    box.onclick = function(e) { if (e.target === box) close(); };
    document.addEventListener("keydown", function(e) { if (e.key === "Escape") close(); });
    document.body.appendChild(box);
    return box;
  }
  function open(id) {
    load(function(l) {
      var ex = null;
      for (var i = 0; i < l.length; i++) if (l[i].id === id || String(l[i].chapter) === String(id)) { ex = l[i]; break; }
      if (!ex) return;
      var b = ensure(), h = '<div class="bar"><b>The Computational Beauty of Nature</b><span>' + ex.title + ' &middot; printed pages ' + (ex.pages[0] - 20) + '&ndash;' + (ex.pages[1] - 20) + '</span><button title="close (Esc)">&times;</button></div>';
      h += '<div class="note">A short excerpt. The book is published by MIT Press.</div>';
      for (var p = ex.pages[0]; p <= ex.pages[1]; p++) h += '<img src="' + root + 'excerpts/' + ex.id + '/' + p + '.png" alt="page ' + (p - 20) + '">';
      b.innerHTML = h; b.querySelector("button").onclick = close;
      b.style.display = "flex"; b.scrollTop = 0;
    });
  }
  function close() { if (box) box.style.display = "none"; }
  return { open: function(id, r) { root = r || ""; open(id); }, close: close,
           has: function(id, cb) { load(function(l) { cb(l.some(function(e) { return e.id === id || String(e.chapter) === String(id); })); }); } };
})();
