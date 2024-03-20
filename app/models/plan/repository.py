from app.models.plan.model import CreatePlan
from app.config.db import getPrisma
from prisma.models import Plan

prisma = getPrisma()

class PlanRepository:

    @staticmethod
    async def getAll():
        return await prisma.prisma.plan.find_many()
    
    @staticmethod
    async def create(plan: CreatePlan):
        return await prisma.prisma.plan.create({
            "title": plan.title,
            "description": plan.description,
            "date_start": plan.date_start,
            "date_end": plan.date_end,
            "user_id": plan.user_id
        })
    
    @staticmethod
    async def getOne(id: int):
        return await prisma.prisma.plan.find_first(where={"plan_id": id})
    
    @staticmethod
    async def delete(id: int):
        return await prisma.prisma.plan.delete(where={"plan_id": id})
    
    @staticmethod
    async def update(id: int, plan: dict):
        return await prisma.prisma.plan.update(where={"plan_id": id}, data=plan)
    
    async def getByUser(user_id: int) -> list[Plan]:
        return await prisma.prisma.plan.find_many(where={"user_id": user_id})