from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

load_dotenv()

environment_variables = os.environ
client = MongoClient(environment_variables["MONGODB_URL"])
db = client["uhl"]
users = db["users"]

class User(BaseModel):
    name: str
    email: str
    

def serialize(mongo_result):
    mongo_result["id"] = str(mongo_result.pop("_id"))
    return mongo_result

# FAST API IMPLEMENTATION
@app.get("/", status_code=200)
def get_all_users():
    result = users.find()
    all_users = []
    for user in result:
        all_users.append(serialize(user))
    return all_users

@app.post("/create", status_code=201)
def create_user(user: User):
    result = users.insert_one(user.model_dump())
    user = users.find_one({ "_id": result.inserted_id})
    serialized_result = serialize(user)
    return { "message": "User has been added", "user": serialized_result}
    
    



# class Handler(BaseHTTPRequestHandler):
#     def _send(self, status, body):
#         self.send_response(status)
#         self.send_header("Content-Type", "application/json")
#         self.end_headers()
#         self.wfile.write(json.dumps(body).encode())
        
        
    
#     def do_GET(self):
#         result = users.find()
#         all_users = []
#         for user in result:
#             all_users.append(serialize(user))
#         self._send(200, all_users)
    
#     # # We want out create path to be /create
#     def do_POST(self):
#         if self.path == "/create":
#             # handle the creation
#             # Read the information from the request body
#             length = int(self.headers.get("Content-Length"))
#             body = json.loads(self.rfile.read(length))
            
#             result = users.insert_one(body)
#             user = users.find_one({ "_id": result.inserted_id})
#             serialized_result = serialize(user)
            
            
            
            
#             self._send(200, { "result": serialized_result})
#         else:
#             self._send(400, { "message": "This path is not supported"})
            
        
        
# if __name__ == "__main__":
#     print("Server is running")
#     HTTPServer(("", 8000), Handler).serve_forever()