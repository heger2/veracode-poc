from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hegertest():
    data = request.get_json()
    if data:
        repo_name = data["repository"]["full_name"]
        ssh_url = data["repository"]["ssh_url"] # Also has html_url and clone_url (https cloning)
        ref = data["ref"] # we should get the sha instead of the branch name in case there's a push between cloning and scanning
        print(f"HEADERS:\n{request.headers}\n")
        print(f"Repo Name: {repo_name}\n")
        print(f"Clone URL: {ssh_url}\n")
        print(f"Ref: {ref}\n")
        return {"message": "success"}

        db = mysql.connector.connect(
            host="localhost",
            user="foo",
            password="bar"
        )

        cursor = db.cursor()
        # Added to test if code analysis tools find the injections vuln
        cursor.execute(f'INSERT INTO footable (name) VALUES ("{repo_name}"")')
        db.commit()
    else:
        return {"message": "hello world"}

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     print("Running...")
#     print("Complete...")
#     return {"message", "Hello World"}

# @app.post("/")
# def veracode_scan():
#     print("Running...")
#     print("Complete...")
#     return {"message", "Hello World"}
