from http.server import HTTPServer, BaseHTTPRequestHandler
import json

users = []

class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())
        
    
    def do_GET(self):
        self._send(200, users)
    
    # # We want out create path to be /create
    def do_POST(self):
        if self.path == "/create":
            # handle the creation
            # Read the information from the request body
            length = int(self.headers.get("Content-Length"))
            body = json.loads(self.rfile.read(length))
            id = len(users) + 1
            users.append({ "id": id, "name": body.get("name"), "email": body.get("email")})
            
            self._send(200, { "message": f"User has been added with ID: {id}"})
        else:
            self._send(400, { "message": "This path is not supported"})
            
        
        



if __name__ == "__main__":
    print("Server is running")
    HTTPServer(("", 8000), Handler).serve_forever()