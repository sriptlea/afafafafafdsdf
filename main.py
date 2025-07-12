from fastapi import FastAPI
import os
import requests
from ro_py.client import Client
from dotenv import load_dotenv
import asyncio
import uvicorn
load_dotenv()

RobloxCookie = os.getenv("COOKIE")
APIKEY = os.getenv("API_KEY")

client = Client(RobloxCookie)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
from fastapi import HTTPException


from fastapi import HTTPException

@app.get("/group/promote/")
async def promote_user(user_name: str, key: str, groupid: int):
    if key != APIKEY:
        return {"error": "Incorrect key"}

    try:
        group = await client.get_group(groupid)
        try:
            usernameinsystem = await client.get_user_by_username(user_name)
        except Exception as e:
            error_str = str(e).lower()
            if "userdoesnotexist" in error_str or "does not exist" in error_str:
                return {"error": f"User '{user_name}' does not exist."}
            raise e

        user_id = usernameinsystem.id
        membertorank = await group.get_member_by_id(user_id)
        await membertorank.promote()
        return {"message": f"User '{user_name}' was promoted!"}

    except Exception as e:
        return {"error": f"Promotion failed: {e}"}
@app.get("/group/demote/")
async def read_items(user_name: str, key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.demote()
     return ("The user was demoted!")
    else:
        return "Incorrect key"
@app.get("/group/rank/")
async def read_items(user_name: str, key: str, groupid: int, role_number: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     target = await group.get_member_by_username(user_name)
     await target.setrole(role_number)
     return ("The user had their ranked changed")
    else:
        return "Incorrect key"
@app.get("/group/members/")
async def read_items(key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     return (group.member_count)
    else:
        return "Incorrect key"
@app.get("/group/membercount/")
async def read_items(key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     return (group.member_count)
    else:
        return "Incorrect key"
@app.get("/group/rankup/")
async def read_items(user_name: str, key: str,groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.promote()
     return ("The user was promoted!")
    else:
        return "Incorrect key"
@app.get("/group/rankdown/")
async def read_items(user_name: str, key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.demote()
     return ("The user was demoted!")
    else:
        return "Incorrect key"
uvicorn.run(app, host="0.0.0.0", port=8080)
