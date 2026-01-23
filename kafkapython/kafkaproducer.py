from kafka import KafkaProducer

producer=KafkaProducer(bootstrap_servers=['localhost:9092'])

future=producer.send('client_topic',
                     b'Helllo,World!')
print('\n',future.get(timeout=60))

future=producer.send('client_topic',
                     key=b'message-two',
                     value=b'This is Kafka-Python')
print('\n',future.get(timeout=60))
