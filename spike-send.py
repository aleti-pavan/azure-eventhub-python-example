import time
import argparse
import sys
from azure.eventhub import EventHubClient, EventData

from utils.env import env
from utils.logging_service import LoggingService

logger = LoggingService('Send').logger

CONNECTION_STRING = env('EVENT_HUB_CONNECTION_STRING')
EVENT_HUB_TOPIC = env('EVENT_HUB_TOPIC_HELLO_WORLD_NAME')
EVENT_HUB_PARTITION = env('EVENT_HUB_TOPIC_HELLO_WORLD_PARTITION')

message = sys.argv[1]


def send():
    client, sender = build_sender_client()

    logger.info(f"Sending message: {message}")

    start_time = time.time()
    sender.send(EventData(message))
    end_time = time.time()

    client.stop()

    run_time = end_time - start_time
    logger.info("Runtime: {} seconds".format(run_time))


def build_sender_client():
    print (CONNECTION_STRING)
    client = EventHubClient.from_connection_string(CONNECTION_STRING, EVENT_HUB_TOPIC)
    sender = client.add_sender(EVENT_HUB_PARTITION)
    client.run()
    return client, sender


if __name__ == "__main__":
    if not CONNECTION_STRING:
        raise ValueError("No EventHubs URL supplied.")

    send()
