from fastapi import APIRouter, Path, Depends
from app.config.schema import ResponseSchema
from app.models.plan.service import PlanService
from app.models.plan.model import CreatePlan, UpdatePlan
from fastapi.exceptions import HTTPException
from app.middlewares.userMiddleware import userMiddleware

router = APIRouter(prefix="/plan", tags=['plan'], dependencies=[Depends(userMiddleware)])

@router.post(
    path="",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To create a vacation plan",
    status_code=201
)
async def createPlan(plan: CreatePlan):
    result = await PlanService.create(payload=plan)
    return ResponseSchema(detail="Successfully create data!", result=result)

@router.get(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To get a plan from database according to id",
    status_code=200
)
async def getPlan(id: int = Path(..., alias="id")):
    result = await PlanService.getOne(id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.get(
    path="/user/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To get all plans from database that belong to a user.",
    status_code=200
)
async def getAllPlans(id: int = Path(..., alias="id")):
    result = await PlanService.getByUser(user_id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.delete(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To delete a plan from database according to id",
    status_code=200
)
async def deletePlan(id: int = Path(..., alias="id")):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await PlanService.delete(id=id)
    return ResponseSchema(detail="Successfully delete data!", result=result)

@router.put(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To update a plan from database according to id",
    status_code=200
)
async def updatePlan(id: int = Path(..., alias="id"), *, plan: UpdatePlan):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await PlanService.update(id=id, plan=plan)
    return ResponseSchema(detail="Successfully update data!", result=result)