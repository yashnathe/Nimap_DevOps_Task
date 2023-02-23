import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")


def read_usersdata():
    with open(datasource, "r") as f:
        content = f.read()
        if content == "":
            content = '{"data": []}'
        users = json.loads(content)
    return users


def add_userdata(user: dict):
    users = read_usersdata()

    with open(datasource, "w") as f:
        if "data" in users:
            users["data"].append(user)
        else:
            users["data"] = [user]

        data = json.dumps(users, indent=2)
        f.write(data)
