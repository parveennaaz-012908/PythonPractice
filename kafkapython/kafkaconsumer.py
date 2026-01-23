from kafka import KafkaConsumer

consumer = KafkaConsumer('client_topic')

for message in consumer:
    print('\n',message)