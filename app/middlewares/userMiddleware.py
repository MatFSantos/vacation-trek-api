from fastapi import Request, HTTPException
from app.utils import token_provider
from jose.exceptions import JWTError, ExpiredSignatureError, JWTClaimsError

# JWTError: If the signature is invalid in any way.
# ExpiredSignatureError: If the signature has expired.
# JWTClaimsError: If any claim is invalid in any way.

async def userMiddleware(req: Request):
    token = req.headers.get('authorization', default=None)
    email = req.headers.get('email', default=None)
    if token and email:
        token = token.split(' ')
        if len(token) == 2 and token[0] == 'Bearer':
            try:
                payload = token_provider.verify(token[1])
            except ExpiredSignatureError:
                raise HTTPException(status_code=403, detail="The signature has expired")
            except JWTClaimsError:
                raise HTTPException(status_code=403, detail="Any claim is invalid.")
            except JWTError:
                raise HTTPException(status_code=403, detail="The signature is invalid.")
            if payload['key'] != email: 
                raise HTTPException(status_code=401, detail="This token is invalid")
        else:
            raise HTTPException(status_code=401, detail="Unauthenticated")
    else:
        raise HTTPException(status_code=401, detail="Unauthenticated because dont have token or email")