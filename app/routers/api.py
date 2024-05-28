from confluent_kafka.avro import SerializerError
from fastapi import APIRouter, HTTPException

from app.broker import avro_consumer

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/consume/")
async def consume():
    try:
        msg = avro_consumer.poll(10)
        if msg is None:
            raise HTTPException(status_code=404, detail="No messages")
        if msg.error():
            raise HTTPException(status_code=500, detail=str(msg.error()))

        return msg.value()
    except SerializerError as e:
        raise HTTPException(
            status_code=500, detail=f"Message deserialization failed: {e}"
        )


@api_router.get("/hello/{name}")
async def hello(name: str):
    return f"Hello, lil {name}"
