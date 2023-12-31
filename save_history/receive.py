import pika, sys, os
import json
from datetime import datetime
import psycopg2


def main(cur):
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

    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(" [x] Received %r" % data, flush=True)
        tm = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        place = data['place']
        weather = json.dumps(data)
        print((tm, place, weather,), flush=True)
        cur.execute("INSERT INTO weather (time, place, weather) VALUES (%s, %s, %s)", (tm, place, weather,))
        conn.commit()
        

    channel.basic_consume(queue='weather', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        conn = psycopg2.connect(host='db', dbname="weather", user="mikhaylov_yv", password="87457")
        cur = conn.cursor()
        main(cur)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)