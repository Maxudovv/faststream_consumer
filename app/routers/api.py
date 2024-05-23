from typing import Annotated

from fast_depends import Depends
from fastapi import APIRouter
from faststream.kafka.fastapi import KafkaRouter, KafkaBroker

from app.broker import broker, router as kafka_router

api_router = APIRouter(prefix="/api", tags=["api"])


@kafka_router.subscriber("hellos_topic")
async def handle_hello(name: str):
    print(f"Someone said hello to {name}!")


@api_router.get("/hello/{name}")
async def hello(name: str):
    return f"Hello, lil {name}"
