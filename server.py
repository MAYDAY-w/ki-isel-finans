import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get('PORT', 3000))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')

class SPARequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def do_GET(self):
        # Serve file if exists, else fallback to index.html for SPA routing
        path = self.translate_path(self.path)
        if not os.path.exists(path) or os.path.isdir(path):
            self.path = '/index.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    print(f"🚀 Python Web Sunucusu çalışıyor: http://0.0.0.0:{PORT} (Klasör: {DIST_DIR})")
    server = HTTPServer(('0.0.0.0', PORT), SPARequestHandler)
    server.serve_forever()
