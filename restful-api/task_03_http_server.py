import http.server
import socketserver
import json


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        if self.path == '/data':
            # 1. Define the dataset
            data = {"name": "John", "age": 30, "city": "New York"}
            # 2. Set response status code
            self.send_response(200)

            # 3. Set the correct JSON header
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # 4. Convert dictionary to JSON string and send
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            # Default response for other paths
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        if self.path == '/status':
            # Implement status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Implement error handling for undefined endpoints
            self.send_error(404, "Endpoint not found")

PORT = 8000
with socketserver.TCPServer(("", PORT), SimpleRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()