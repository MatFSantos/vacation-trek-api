from functools import lru_cache
from prisma import Prisma

class PrismaConnection:

    def __init__(self) -> None:
        self.prisma = Prisma()
    
    async def connect(self):
        await self.prisma.connect()

    async def disconnect(self):
        await self.prisma.disconnect()

@lru_cache
def getPrisma():
    return PrismaConnection()