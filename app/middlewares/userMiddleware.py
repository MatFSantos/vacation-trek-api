from fastapi import Request, HTTPException
from app.utils import token_provider
from jose.exceptions import JWTError, ExpiredSignatureError, JWTClaimsError

async def userMiddleware(req: Request):
    token = req.headers.get('Authorization', default=None)
    if token:
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
            return payload['key']
        else:
            raise HTTPException(status_code=401, detail="Unauthenticated")
    else:
        raise HTTPException(status_code=401, detail="Unauthenticated")