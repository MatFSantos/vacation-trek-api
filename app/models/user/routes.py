from fastapi import APIRouter, Request, Path, Depends
from app.config.schema import ResponseSchema
from app.models.user.service import UserService
from app.models.user.model import CreateUser, UpdateUser, LoginUser, VerifyUser
from fastapi.exceptions import HTTPException
from app.middlewares.userMiddleware import userMiddleware

router = APIRouter(prefix="/user", tags=['user'])

@router.post(
    path="/login",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To login an user.",
    status_code=200
)
async def loginUser(user: LoginUser):
    result = await UserService.login(payload=user)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.get(
    path="/{id}",
    response_model=ResponseSchema,
    dependencies=[Depends(userMiddleware)],
    response_model_exclude_none=True,
    description="To get a user from database according to id",
    status_code=200
)
async def getUser(id: int = Path(..., alias="id")):
    result = await UserService.getOne(id=id)
    return ResponseSchema(detail="Successfully get data!", result=result)

@router.post(
    path="",
    response_model=ResponseSchema,
    response_model_exclude_none=True,
    description="To create a user",
    status_code=201
)
async def createUser(user: CreateUser):
    result = await UserService.create(payload=user)
    return ResponseSchema(detail="Successfully create data!", result=result)

@router.delete(
    path="/{id}",
    response_model=ResponseSchema,
    dependencies=[Depends(userMiddleware)],
    response_model_exclude_none=True,
    description="To delete a user from database according to id",
    status_code=200
)
async def deleteUser(id: int = Path(..., alias="id")):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await UserService.delete(id=id)
    return ResponseSchema(detail="Successfully delete data!", result=result)

@router.put(
    path="/{id}",
    response_model=ResponseSchema,
    dependencies=[Depends(userMiddleware)],
    response_model_exclude_none=True,
    description="To update a user from database according to id",
    status_code=200
)
async def updateUser(id: int = Path(..., alias="id"), *, user: UpdateUser):
    raise HTTPException(status_code=405, detail="This method is yet to be implemented.")
    result = await UserService.update(id=id, user=user)
    return ResponseSchema(detail="Successfully update data!", result=result)

@router.post(
    path="/verify-login",
    response_model=ResponseSchema,
    dependencies=[Depends(userMiddleware)],
    response_model_exclude_none=True,
    description="To verify if a user is correctly loged",
    status_code=200
)
async def verifyUser(email: str = Depends(userMiddleware)):
    result = await UserService.getByEmail(email=email)
    return ResponseSchema(detail="User loged", result=result)