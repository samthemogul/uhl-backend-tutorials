# GET /google.com

# 1. Method: GET, POST, PUT, PATCH, DELETE
# 2. Path: google.com, /

# HTTP Security over TLS/SSL


# GET http://api.github.com/users/samthemogul "https://"
# from urllib.request import urlopen
# import json

# response = urlopen("https://api.github.com/users/samthemogul")
# print(json.load(response))

# Comp A -> JSON.encode(SAM)   -> 1010101010110
# COMP B -> 0101010101010 -> JSON>decode(0101010101) -> SAM
# JSON

# OBJECT ORIENTED PROGRAMMING



from http.server import BaseHTTPRequestHandler, HTTPServer

samuel_data = {"name": "Samuel", "age": 15, "is_married": False}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response code
        # Sednd response body
        self.send_response(200, samuel_data)
        
# PORTS
# 176:13618:8316/80, 433, 
# POSTMAN
HTTPServer(("", 8000), Handler).serve_forever()



