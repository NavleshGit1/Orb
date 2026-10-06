import http.server
import socketserver
import os
import urllib.parse
import mimetypes
import sys
import webbrowser

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('model/gltf-binary', '.glb')
mimetypes.add_type('application/octet-stream', '.basis')
mimetypes.add_type('application/json', '.json')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('audio/ogg', '.ogg')
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('video/webm', '.webm')

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Decode url for logging and resolving
        decoded_path = urllib.parse.unquote(self.path)
        super().do_GET()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"==================================================")
        print(f"  ORBITRA'26 Local Server Running")
        print(f"  URL: http://localhost:{PORT}")
        print(f"  Directory: {DIRECTORY}")
        print(f"==================================================")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == '__main__':
    run_server()
