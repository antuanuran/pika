import pika
import json


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


def callback_tg(ch, method, properties, body):
    print(body)


# Подписка на очередь
queue_telegram = "telegram_message_queue"
channel.basic_consume(
    queue=queue_telegram, on_message_callback=callback_tg, auto_ack=True
)

# Запуск консьюм-ожидания сообщения
channel.start_consuming()
