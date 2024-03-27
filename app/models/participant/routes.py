from fastapi import APIRouter, Path, Depends
from app.config.schema import ResponseSchema
from app.models.participant.service import ParticipantService
from app.models.participant.model import CreateParticipant, UpdateParticipant
from fastapi.exceptions import HTTPException
from app.middlewares.userMiddleware import userMiddleware

router = APIRouter(prefix="/participant", tags=['participant'], dependencies=[Depends(userMiddleware)])

@router.get(
    path="/{id}",
    response_model=ResponseSchema,
    dependencies=[Depends(userMiddleware)],
    response_model_exclude_none=True,
    description="To get a participant from database according to id",
    status_code=200
)
async def getParticipant(id: int = Path(..., alias="id")):
    result = await ParticipantService.getOne(id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.post(
    path="",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To create a participant",
    status_code=201
)
async def createParticipant(participant: CreateParticipant):
    result = await ParticipantService.create(payload=participant)
    return ResponseSchema(detail="Successfully create data!", result=result)

@router.get(
    path="/plan/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To get all participants from database that belong to a plan.",
    status_code=200
)
async def getAllParticipant(id: int = Path(..., alias='id')):
    result = await ParticipantService.getByPlan(plan_id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.delete(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To delete a participant from database according to id",
    status_code=200
)
async def deleteParticipant(id: int = Path(..., alias="id")):
    result = await ParticipantService.delete(id=id)
    return ResponseSchema(detail="Successfully delete data!", result=result)

@router.put(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To update a participant from database according to id",
    status_code=200
)
async def updateParticipant(id: int = Path(..., alias="id"), *, participant: UpdateParticipant):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await ParticipantService.update(id=id, participant=participant)
    return ResponseSchema(detail="Successfully update data!", result=result)