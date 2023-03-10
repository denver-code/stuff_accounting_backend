import jwt
import datetime

from fastapi import HTTPException, Header

class FastJWT:
    def __init__(self):
        self.secret_key = ""


    def set_secret_key(self, secret_key):
        self.secret_key = secret_key


    async def encode(self, optional_data=None, expire=None):
        if not expire:
            expire = (datetime.datetime.now() + datetime.timedelta(days=30)).timestamp()

        token_json = {
            "expire": expire
        }

        if optional_data:
            token_json.update(optional_data)
        jwt_token = jwt.encode(token_json, self.secret_key, algorithm="HS256")

        return jwt_token
    

    async def decode(self, payload):
        return jwt.decode(payload, self.secret_key, algorithms=["HS256"])


    async def login_required(self, Authorisation=Header("Authorisation")):
        try:
            if Authorisation == "Authorisation":
                raise
            
            jwt_token = await self.decode(Authorisation)

            if jwt_token["expire"] < int(datetime.datetime.now().timestamp()):
                raise

        except:
            raise HTTPException(status_code=401, detail="Unauthorized.")