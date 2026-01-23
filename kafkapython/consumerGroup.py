from kafka import KafkaConsumer
from kafka.consumer import group
import json

if __name__ == "__main__":
    

    consumer = KafkaConsumer(
        "customer_details",
        bootstrap_servers=["localhost:9092"],
        group_id="ConsumerGroupA"

    )
    print("Consumer Started")

    for i in consumer:
        print(f"consumer data{ json.loads(i.value)}")
