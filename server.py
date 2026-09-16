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

# TODO
# Host, PORTS, HEADERS, BODY, STATUS CODES, CONTENT/MIME TYPES

# 



# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json

# samuel_data = {"name": "Samuel", "age": 15, "is_married": False}

# class Handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         # Send response code
#         # Sednd response body
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(json.dumps(samuel_data).encode())
        
# # PORTS
# # 176:13618:8316/80, 433, 
# # POSTMAN
# port = 8000
# if __name__ == "__main__":
#     print("Server is running on port: ", port)
#     HTTPServer(("", port), Handler).serve_forever()
    



