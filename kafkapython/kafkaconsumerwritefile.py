from kafka import KafkaConsumer
import csv
from datetime import datetime
import os

consumer = KafkaConsumer('client_topic')

if os.path.isfile("msg.csv"):
    print("File already exist...\n deleting the file")
    os.remove("msg.csv")

with open('msg.csv', 'a') as f:
    file_writer=csv.writer(f)
    file_writer.writerow(['timestamp','message'])
    print("CSV file initialized")

    for message in consumer:
        msg = str(message.value.decode())
        ts= datetime.fromtimestamp(message.timestamp/1000).strftime("%A,%B %d,%Y %I:%M:%S")

        print("Writing message %s..", msg)
        file_writer.writerow([ts,msg])
print("File written successfully")
f.close()


