import logging
from app.orm import db
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from app.orm.db_setup import database, engine
from app.api.purchase_api import purchase_api

db.metadata.create_all(engine)

async def startup():
    await database.connect()
    logger.info("Anantarupa service is up!!!")

async def shutdown():
    logger.info("shutting down Anantarupa service...")

@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

@app.get("/alive")
async def getInfo():
    return {
        "desc":"Microservices for Ananta in-game shop"
    }

app.include_router(purchase_api, tags=["Shop Items"])
