from fastapi import APIRouter, Depends, HTTPException, Request
from app.core.tools.jwt import FastJWT
from app.core.tools.database import find_one, update_one, delete_one
from v1.models.item import Item as ItemModel
from v1.schemas.item import Item as ItemSchema
from app.core.tools.check import is_valid_id
from bson import ObjectId

items_router = APIRouter(prefix="/items")

@items_router.post("/new")
async def new_item_event(item: ItemSchema, request: Request):
    auth_token = request.headers["Authorisation"]
    auth_token = await FastJWT().decode(auth_token)
    user = await find_one("users_db", {"email": auth_token["email"]})
    _item = ItemModel(
        title=item.title,
        description=item.description,
        picture=item.picture,
        owner= str(user["_id"])
    )
    _result = await _item.insert()

    _item = _item.dict()
    _item["_id"] = str(_result.inserted_id)

    if not any(_item["_id"] == i.get("id") for i in user["saved"]):
        user["saved"].append({
            "id": _item["_id"],
            "tag": item.tag
        })
        await update_one("users_db", {"email": auth_token["email"]}, user)

    return _item


@items_router.post("/{id}")
async def find_item_event(id: str, request: Request):
    if not is_valid_id(id):
        raise HTTPException(400, "ID are invalid.")
    
    auth_token = request.headers["Authorisation"]
    auth_token = await FastJWT().decode(auth_token)

    user = await find_one("users_db", {"email": auth_token["email"]})
    if not any(id == i.get("id") for i in user["saved"]):
        raise HTTPException(403, "You don't have access to this item.")
    
    item = await find_one("items_db", {"_id": ObjectId(id)})
    item["_id"] = str(item["_id"])

    return  item


@items_router.delete("/{id}")
async def find_item_event(id: str, request: Request):
    if not is_valid_id(id):
        raise HTTPException(400, "ID are invalid.")
    
    auth_token = request.headers["Authorisation"]
    auth_token = await FastJWT().decode(auth_token)
    user = await find_one("users_db", {"email": auth_token["email"]})
    
    item = await find_one("items_db", {"_id": ObjectId(id)})
    if item["owner"] != str(user["_id"]):
        raise HTTPException(403, "You don't have access to changing this item.")
    
    for _item in user["saved"]:
        if _item["id"] == id:
            del user["saved"][user["saved"].index(_item)]
            break
    
    await update_one("users_db", {"email": auth_token["email"]}, user)
    await delete_one("items_db", {"_id": ObjectId(id)})

    return  {"message": "Deleted."}



@items_router.post("/upc")
async def new_upc_item_event(item: ItemSchema):
    _item = ItemModel(item)
    _result = await _item.insert()
    print(_result)
    return _item.dict()

