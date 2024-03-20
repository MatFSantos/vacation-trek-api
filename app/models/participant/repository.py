from app.models.participant.model import CreateParticipant
from app.config.db import getPrisma
from prisma.models import Participant

prisma = getPrisma()

class ParticipantRepository:

    @staticmethod
    async def getAll() -> list[Participant]:
        return await prisma.prisma.participant.find_many()
    
    @staticmethod
    async def create(participant: CreateParticipant) -> Participant:
        return await prisma.prisma.participant.create({
            "name": participant.name,
            "plan_id": participant.plan_id,
        })
    
    @staticmethod
    async def getOne(id: int) -> Participant | None:
        return await prisma.prisma.participant.find_first(where={"participant_id": id})
    
    @staticmethod
    async def delete(id: int) -> Participant | None:
        return await prisma.prisma.participant.delete(where={"participant_id": id})
    
    @staticmethod
    async def update(id: int, participant: dict) -> Participant | None:
        return await prisma.prisma.participant.update(where={"participant_id": id}, data=participant)
    
    @staticmethod
    async def getByPlan(plan_id: int) -> list[Participant]:
        return await prisma.prisma.participant.find_many(where={"plan_id": plan_id})