from fastapi import HTTPException
import requests
import json


async def get_item(ucp: str):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip,deflate',
    }
    resp = requests.get(f'https://api.upcitemdb.com/prod/trial/lookup?upc={ucp}', headers=headers)
    data = json.loads(resp.text)

    if resp.status_code in [404, 400]:
        raise HTTPException(resp.status_code, data["message"])

    if not data["items"]:
        raise HTTPException(404, "Unfortunately product not found.")
    
    del data["items"][0]["offers"]

    return data["items"][0]
    