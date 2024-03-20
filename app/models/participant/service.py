from app.models.participant.repository import ParticipantRepository
from app.models.participant.model import CreateParticipant
from app.models.plan.repository import PlanRepository
from fastapi.exceptions import HTTPException

class ParticipantService:

    @staticmethod
    async def getAll():
        try:
            return await ParticipantRepository.getAll()
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def getOne(id: int):
        try:
            result = await ParticipantRepository.getOne(id=id)
            return result
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def delete(id: int):
        try:
            return await ParticipantRepository.delete(id=id)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def update(id: int, participant: dict):
        try:
            return await ParticipantRepository.update(id=id, participant=participant)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")

    @staticmethod
    async def create(payload: CreateParticipant):
        searcher = await PlanRepository.getOne(id=payload.plan_id)
        if searcher is None:
            raise HTTPException(status_code=404, detail="Plan don't exists")
        
        try:
            return await ParticipantRepository.create(participant=payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")

    @staticmethod
    async def getByPlan(plan_id: int):
        searcher = await PlanRepository.getOne(id=plan_id)
        if searcher is None:
            raise HTTPException(status_code=404, detail="Plan don't exists")
        
        try:
            return await ParticipantRepository.getByPlan(plan_id=plan_id)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
