import json
import pika

QUEUE = "hello-queue"
MESSAGE = {
    "transactionId": "TX123456",
    "timestamp": "2026-06-01T10:15:30",
    "senderBank": "BankA",
    "receiverBank": "BankB",
    "senderAccount": "12345",
    "receiverAccount": "98765",
    "amount": 1500.50,
}
body = json.dumps(MESSAGE)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue=QUEUE, durable=True)

channel.basic_publish(
    exchange="",
    routing_key=QUEUE,
    body=body,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
        content_type="application/json",
    ),
)

print(f"Sent: {body}")
connection.close()
