from fastapi import FastAPI
from app.config.settings import getSettings
from app.config.db import getPrisma

settings = getSettings()
prisma = getPrisma()


"""Creating App"""
def get_app():
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
    )

    async def startup():
        await prisma.connect()
        print("DB:\t  Start Database connection.")

    async def shutdown():
        await prisma.disconnect()
        print("DB:\t  Shutdown Database connection.")

    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)

    return app