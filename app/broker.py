from confluent_kafka.avro import AvroConsumer
from confluent_kafka import avro
from pydantic import BaseModel

schema_registry_url = 'http://schema-registry:8081'
kafka_broker = 'kafka:9092'
topic = 'greetings'

value_schema_str = """
{
  "namespace": "greetings",
  "type": "record",
  "name": "Greeting",
  "fields": [
    {"name": "name", "type": "string"}
  ]
}
"""
value_schema = avro.loads(value_schema_str)

avro_consumer_config = {
    'bootstrap.servers': kafka_broker,
    'schema.registry.url': schema_registry_url,
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest'
}
avro_consumer = AvroConsumer(avro_consumer_config)
avro_consumer.subscribe([topic])


class User(BaseModel):
    name: str
