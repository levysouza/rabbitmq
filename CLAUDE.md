# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

RabbitMQ must be running locally on the default port (5672).

## Running

Run the producer to publish a message, then the consumer to receive it:

```bash
python producer.py
python consumer.py   # blocks waiting for messages; Ctrl+C to exit
```

## Architecture

This is a minimal RabbitMQ producer/consumer example using `pika` (the Python AMQP client).

- **`producer.py`** — connects to localhost RabbitMQ, declares a durable queue (`hello-queue`), and publishes a single JSON-encoded financial transaction message with persistent delivery mode, then closes.
- **`consumer.py`** — connects to the same queue, sets `prefetch_count=1` for fair dispatch, and blocks consuming messages. Each message is JSON-decoded and manually acknowledged after processing.

Both scripts declare the queue with `durable=True` so it survives broker restarts. The producer sets `delivery_mode=Persistent` so messages survive restarts as well.
