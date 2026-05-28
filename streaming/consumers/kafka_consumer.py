from kafka import KafkaConsumer
import json
from config.settings import KAFKA_BOOTSTRAP_SERVERS


class SportsKafkaConsumer:
    def __init__(self, topic: str, group_id: str = "sports-consumer-group"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset="earliest",
            group_id=group_id,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

    def consume(self):
        for message in self.consumer:
            yield message.value

    def close(self) -> None:
        self.consumer.close()
