from app.models.user.model import CreateUser
from app.config.db import getPrisma
from prisma.models import User

prisma = getPrisma()

class UserRepository:

    @staticmethod
    async def getAll():
        return await prisma.prisma.user.find_many()
    
    @staticmethod
    async def create(user: CreateUser):
        return await prisma.prisma.user.create({
            "name": user.name,
            "email": user.email,
            "password": user.password
        })
    
    @staticmethod
    async def getOne(id: int):
        return await prisma.prisma.user.find_first(where={"user_id": id})
    
    @staticmethod
    async def delete(id: int):
        return await prisma.prisma.user.delete(where={"user_id": id})
    
    @staticmethod
    async def update(id: int, user: dict):
        return await prisma.prisma.user.update(where={"user_id": id}, data=user)
    
    @staticmethod
    async def getByEmail(email: str) -> User | None:
        return await prisma.prisma.user.find_first(where={"email": email})