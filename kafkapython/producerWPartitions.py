from kafkaproducer import KafkaProducer
import json
import time
from consumer_data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
def get_partition(key_bytes,all_partition, available_partition):
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition)

if __name__ =="__main__":
    while True:
        user_data= get_registered_user()
        print(user_data)

        producer.send(topic="customer_details", value=user_data)

        time.sleep(3)
