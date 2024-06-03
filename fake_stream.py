import pika
import json
from datetime import datetime

# 0. Параметры подключения pika
connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",
    credentials=pika.PlainCredentials(username="admin", password="pass"),
)

# 1. Установка соединения. Используем библиотеку - pika в роли клиентской библиотеки
connection = pika.BlockingConnection(connection_params)

# 2. Создание канала для работы с RabbitMQ
channel = connection.channel()

cam_id = 666
# channel.queue_declare(queue=f"{cam_id}", durable=True)

# 4. Отправили проверочное письмо
current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

message_json = {
    "img": [255, 158, 56, 45],
    "time": current_time,
    "cam": cam_id,
    "location_description": "55,755831°, 37,617673°",
    "meta": {
        "events": {
            "cls": "knife",
            "conf": "89 %",
            "text": "description",
            "model": "Bosh-404",
        }
    },
}

channel.basic_publish(
    exchange="", routing_key="666", body=json.dumps(message_json)
)
