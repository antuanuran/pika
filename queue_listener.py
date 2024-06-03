import json

import pika


# 0. Параметры подключения pika
connection_params = pika.ConnectionParameters(
    host="rabbit",
    port=5672,
    virtual_host="/",
    credentials=pika.PlainCredentials(username="admin", password="pass"),
)

# 1. Установка соединения. Используем библиотеку - pika в роли клиентской библиотеки
connection = pika.BlockingConnection(connection_params)

# 2. Создание канала для работы с RabbitMQ
channel = connection.channel()

# 3.  Создание очередей - queue_declare()
channel.queue_declare(queue="666", durable=True)


# 6. Функция, которая будет вызвана каждый раз, когда сообщение будет получено из очереди.
def callback(ch, method, properties, body):
    json_data = body.decode("utf-8")
    data = json.loads(json_data)
    print(data)

    queue_telegram = "telegram_message_queue"
    channel.queue_declare(queue=queue_telegram)
    channel.basic_publish(
        exchange="",
        routing_key=queue_telegram,
        body=json.dumps(data),
    )

    queue_frontend = "frontend_message_queue"
    channel.queue_declare(queue=queue_frontend)
    channel.basic_publish(
        exchange="",
        routing_key=queue_frontend,
        body=json.dumps(data),
    )


# 4. Подписка на очередь - basic_consume()
channel.basic_consume(queue="666", on_message_callback=callback, auto_ack=True)

# 5. Старт Consuming. Запуск ожидания сообщения в очередь
channel.start_consuming()
