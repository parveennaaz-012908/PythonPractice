from kafkaproducer import KafkaProducer
import json
import time
from consumer_data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ =="__main__":
    while True:
        user_data= get_registered_user()
        print(user_data)

        producer.send(topic="customer_details", value=user_data)

        time.sleep(2)
