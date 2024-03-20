from app.models.itinerary.repository import ItineraryRepository
from app.models.itinerary.model import CreateItinerary
from app.models.plan.repository import PlanRepository
from fastapi.exceptions import HTTPException

class ItineraryService:

    @staticmethod
    async def getAll():
        return await ItineraryRepository.getAll()
    
    @staticmethod
    async def getOne(id: int):
        result = await ItineraryRepository.getOne(id=id)
        return result
    
    @staticmethod
    async def delete(id: int):
        return await ItineraryRepository.delete(id=id)
    
    @staticmethod
    async def update(id: int, itinerary: dict):
        return await ItineraryRepository.update(id=id, itinerary=itinerary)

    @staticmethod
    async def create(payload: CreateItinerary):
        searcher = await PlanRepository.getOne(id=payload.plan_id)
        if searcher is None:
            raise HTTPException(status_code=404, detail="Plan don't exists")

        try:
            itinerary = await ItineraryRepository.create(itinerary=payload)
            return itinerary
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def getByPlan(plan_id: int):
        searcher = await PlanRepository.getOne(id=plan_id)
        if searcher is None:
            raise HTTPException(status_code=404, detail="Plan don't exists")

        try:
            return ItineraryRepository.getByPlan(plan_id=plan_id)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")