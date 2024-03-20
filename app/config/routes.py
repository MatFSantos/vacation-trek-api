from fastapi import FastAPI
from app.config.settings import getSettings

from app.models.user.routes import router as userRouter
from app.models.plan.routes import router as planRouter
from app.models.participant.routes import router as participantRouter
from app.models.itinerary.routes import router as itineraryRouter

settings = getSettings()

def init_routes(app: FastAPI):
    app.include_router(userRouter)
    app.include_router(planRouter)
    app.include_router(participantRouter)
    app.include_router(itineraryRouter)