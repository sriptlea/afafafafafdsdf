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

import traceback
from fastapi import HTTPException

@app.get("/group/promote/")
async def promote_user(user_name: str, key: str, groupid: int):
    if key != APIKEY:
        raise HTTPException(status_code=401, detail="Incorrect key")

    try:
        group = await client.get_group(groupid)
        usernameinsystem = await client.get_user_by_username(user_name)
        user_id = usernameinsystem.id
        membertorank = await group.get_member_by_id(user_id)
        await membertorank.promote()
        return {"message": "The user was promoted!"}
    except Exception as e:
        tb_str = traceback.format_exc()
        print(f"Promotion error:\n{tb_str}")  # Logs full traceback to console/log
        raise HTTPException(status_code=500, detail=f"Promotion failed: {e.__class__.__name__}: {str(e)}")
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
