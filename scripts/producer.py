import argparse
import json
import random
from datetime import datetime
from time import sleep

from kafka import KafkaProducer
from kafka.errors import KafkaError


def create_data():
    return {
        "measurement": "tsdata",
        "tags": {
            "client_id": "CZFGE",
            "machine_id": "MDZFZ",
            "ligne_id": "DZG",
            "mesure_id": "ZPFLEGG",
        },
        "time": datetime.now(),
        "fields": {
            "b_value": random.randint(60, 90),
            "c_value": random.randint(70, 120),
        },
    }


def send_data(producer: KafkaProducer, topic: str) -> None:
    producer.send(topic, create_data())

    producer.flush()


def main(topic: str) -> None:
    producer = KafkaProducer(
        bootstrap_servers="172.17.0.1:9093",
        value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8"),
    )

    while True:
        send_data(producer, topic)
        sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("create_topic")
    parser.add_argument("topic", help="Topic name", type=str)
    args = parser.parse_args()
    try:
        main(args.topic)
    except KafkaError as error:
        print(error)
