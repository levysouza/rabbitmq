# Rabbitmq

Exemplo mínimo de produtor e consumidor com RabbitMQ usando Python e a biblioteca `pika`: o `producer.py` conecta ao broker local, declara uma fila durável (`hello-queue`) e publica uma mensagem JSON simulando uma transação financeira com entrega persistente; o `consumer.py` consome essa mesma fila com `prefetch_count=1` para despacho justo, processa cada mensagem e envia o acknowledgement manual, garantindo que nenhuma mensagem seja perdida em caso de falha. 

Para rodar, ative o virtualenv (`python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`), certifique-se de que o RabbitMQ está rodando na porta 5672 e execute `python producer.py` seguido de `python consumer.py`.