from faststream.kafka.fastapi import KafkaRouter

router = KafkaRouter("localhost:9092")


def broker():
    return router.broker
