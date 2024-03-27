from fastapi import APIRouter, Path, Depends
from app.config.schema import ResponseSchema
from app.models.itinerary.service import ItineraryService
from app.models.itinerary.model import CreateItinerary, UpdateItinerary
from fastapi.exceptions import HTTPException
from app.middlewares.userMiddleware import userMiddleware

router = APIRouter(prefix="/itinerary", tags=['itinerary'], dependencies=[Depends(userMiddleware)])

@router.post(
    path="",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To create a itinerary in vacation plan",
    status_code=201
)
async def createItinerary(itinerary: CreateItinerary):
    result = await ItineraryService.create(payload=itinerary)
    return ResponseSchema(detail="Successfully create data!", result=result)

@router.get(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To get a itinerary from database according to id",
    status_code=200
)
async def getItinerary(id: int = Path(..., alias="id")):
    result = await ItineraryService.getOne(id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.get(
    path="/plan/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To get all itineraries from database that belong to a vacation plan.",
    status_code=200
)
async def getAllItineraries(id: int = Path(..., alias="id")):
    result = await ItineraryService.getByPlan(plan_id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.delete(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To delete a itinerary from database according to id",
    status_code=200
)
async def deleteItinerary(id: int = Path(..., alias="id")):
    result = await ItineraryService.delete(id=id)
    return ResponseSchema(detail="Successfully delete data!", result=result)

@router.put(
    path="/{id}",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To update a itinerary from database according to id",
    status_code=200
)
async def updateItinerary(id: int = Path(..., alias="id"), *, itinerary: UpdateItinerary):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await ItineraryService.update(id=id, itinerary=itinerary)
    return ResponseSchema(detail="Successfully update data!", result=result)