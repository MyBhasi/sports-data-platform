from kafka import KafkaProducer
import json
from config.settings import KAFKA_BOOTSTRAP_SERVERS


class SportsKafkaProducer:
    def __init__(self, topic: str):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send(self, message: dict) -> None:
        self.producer.send(self.topic, value=message)
        self.producer.flush()

    def close(self) -> None:
        self.producer.close()
