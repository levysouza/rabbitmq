import json
import pika

QUEUE = "hello-queue"


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f"Received: {json.dumps(message, indent=2)}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

print("Waiting for messages. To exit press CTRL+C")
channel.queue_declare(queue=QUEUE, durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE, on_message_callback=callback)
channel.start_consuming()
