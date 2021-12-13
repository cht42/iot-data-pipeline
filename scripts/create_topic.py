import argparse

from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError


def main(topic: str) -> None:
    admin_client = KafkaAdminClient(bootstrap_servers="172.17.0.1:9093")

    admin_client.create_topics(
        [NewTopic(name=topic, num_partitions=1, replication_factor=1)]
    )
    print(f"Topic [{topic}] successfully created !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("create_topic")
    parser.add_argument("topic", help="Topic name", type=str)
    args = parser.parse_args()
    try:
        main(args.topic)
    except KafkaError as error:
        print(error)
