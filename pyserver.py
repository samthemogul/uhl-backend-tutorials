from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

DATA_FILE = "users.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as user_data:
        return json.load(user_data)

def write_users(users):
    with open(DATA_FILE, 'w') as user_data:
        json.dump(users, user_data)


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())
        
    
    def do_GET(self):
        users = load_users()
        self._send(200, users)
    
    # # We want out create path to be /create
    def do_POST(self):
        if self.path == "/create":
            # handle the creation
            # Read the information from the request body
            length = int(self.headers.get("Content-Length"))
            body = json.loads(self.rfile.read(length))
            existing_users = load_users()
            id = len(existing_users) + 1
            
            
            existing_users.append({ "id": id, "name": body.get("name"), "email": body.get("email")})
            write_users(existing_users)
            
            self._send(200, { "message": f"User has been added with ID: {id}"})
        else:
            self._send(400, { "message": "This path is not supported"})
            
        
        



if __name__ == "__main__":
    print("Server is running")
    HTTPServer(("", 8000), Handler).serve_forever()