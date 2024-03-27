from app.models.itinerary.model import CreateItinerary
from app.config.db import getPrisma
from prisma.models import Itinerary

prisma = getPrisma()

class ItineraryRepository:

    @staticmethod
    async def getAll() -> list[Itinerary]:
        return await prisma.prisma.itinerary.find_many()
    
    @staticmethod
    async def create(itinerary: CreateItinerary) -> Itinerary:
        return await prisma.prisma.itinerary.create({
            "date": itinerary.date,
            "location": itinerary.location,
            "plan_id": itinerary.plan_id
        })
    
    @staticmethod
    async def getOne(id: int) -> Itinerary | None:
        return await prisma.prisma.itinerary.find_first(where={"itinerary_id": id})
    
    @staticmethod
    async def delete(id: int) -> Itinerary | None:
        return await prisma.prisma.itinerary.delete(where={"itinerary_id": id})
    
    @staticmethod
    async def update(id: int, itinerary: dict) -> Itinerary | None:
        return await prisma.prisma.itinerary.update(where={"itinerary_id": id}, data=itinerary)
    
    @staticmethod
    async def getByPlan(plan_id: int) -> list[Itinerary]:
        return await prisma.prisma.itinerary.find_many(where={"plan_id": plan_id}, order={'date': 'asc'})