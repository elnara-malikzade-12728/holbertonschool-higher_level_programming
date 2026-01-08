import http.server
import socketserver
import json


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Use an if/elif structure to ensure only ONE block executes per request
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Ensure the JSON is dumped correctly to a string then encoded
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Handle all other undefined endpoints with a 404
            self.send_error(404, "Endpoint Not Found")


# Define the port
PORT = 8000

# Using Allow Reuse Address helps prevent "Address already in use" errors during rapid restarts
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), SimpleRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")