#!/usr/bin/env python3
"""Static dev server that forbids caching (python http.server otherwise lets
Chrome keep stale pages).  usage: python3 tools/serve.py [port]"""
import sys, os, http.server
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(("", int(sys.argv[1]) if len(sys.argv) > 1 else 8767), H).serve_forever()
