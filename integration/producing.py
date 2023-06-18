import pika
import time
import get_wether
import json

credentials = pika.PlainCredentials('mikhaylov_yv', '87457')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'rabbitmq', 
        5672, 
        '/',
        credentials=credentials 
        )
    )
channel = connection.channel()
channel.queue_declare(queue='weather')

while True:
    weather = get_wether.get_wether()
    channel.basic_publish(exchange='',
                      routing_key='weather',
                      body=json.dumps(weather))
    time.sleep(60)
