from app.models.plan.repository import PlanRepository
from app.models.user.repository import UserRepository
from app.models.plan.model import CreatePlan
from fastapi.exceptions import HTTPException
from prisma.models import Plan

class PlanService:

    @staticmethod
    async def getAll() -> list[Plan]:
        try:
            return await PlanRepository.getAll()
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def getOne(id: int) -> Plan:
        try:
            result = await PlanRepository.getOne(id=id)
            return result
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")
    
    @staticmethod
    async def delete(id: int) -> Plan | None:
        try:
            return await PlanRepository.delete(id=id)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")


    @staticmethod
    async def update(id: int, plan: dict) -> Plan | None:
        try:
            return await PlanRepository.update(id=id, plan=plan)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")

    @staticmethod
    async def create(payload: CreatePlan) -> Plan:
        searcher = await UserRepository.getOne(id=payload.user_id)
        if searcher is None:
            raise HTTPException(status_code=404, detail="User don't exists")

        try:
            return await PlanRepository.create(plan=payload)
        except Exception as e:
            HTTPException(status_code=500, detail=f"An error was occurred: {str(e)}")

    @staticmethod
    async def getByUser(user_id: int) -> list[Plan]:
        plans = await PlanRepository.getByUser(user_id=user_id)
        return plans