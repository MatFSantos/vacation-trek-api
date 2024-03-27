from app.models.user.repository import UserRepository
from app.models.user.model import CreateUser, LoginUser
from fastapi.exceptions import HTTPException
from app.utils import hash_provider, token_provider

class UserService:

    @staticmethod
    async def getAll():
        try:
            return await UserRepository.getAll()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def getOne(id: int):
        try:
            result = await UserRepository.getOne(id=id)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
        if result:
            result.password = None
            return result
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    
    @staticmethod
    async def delete(id: int):
        try:
            return await UserRepository.delete(id=id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def update(id: int, user: dict):
        try:
            return await UserRepository.update(id=id, user=user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def login(payload: LoginUser):
        searcher = await UserRepository.getByEmail(payload.email)
        if searcher is None:
            raise HTTPException(status_code=400, detail="E-mail not founded")
        
        if not hash_provider.verify(text=payload.password, hash=searcher.password):
            raise HTTPException(status_code=403, detail="Incorrect password.")

        token = token_provider.generate({'key': searcher.email})
        searcher.password = None
        return {"user": searcher, "token": token}

    @staticmethod
    async def create(payload: CreateUser):
        searcher = await UserRepository.getByEmail(payload.email)
        if searcher is not None:
            raise HTTPException(status_code=400, detail="E-mail already exists")
        new_pass = hash_provider.generate(payload.password)
        payload.password = new_pass

        try:
            new_user = await UserRepository.create(user=payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")

        token = token_provider.generate({'key': new_user.email})
        new_user.password = None
        return {"user": new_user, "token": token}
    
    @staticmethod
    async def getByEmail(email: str):
        try:
            result = await UserRepository.getByEmail(email=email)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
        if result:
            result.password = None
            return result
        else:
            raise HTTPException(status_code=404, detail="User not found.")
        