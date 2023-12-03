import random
import time
import json

from paho.mqtt import client as mqtt_client


broker = 'mixko50.trueddns.com'
port = 25836
topic = 'KMUTT/Helmet_Detector'
#Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'helmet'
password = 'mixko00112233'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,data):
    if data:
        time.sleep(1)
        result = client.publish(topic, data)
        status = result[0]
        if status == 0:
            print(f"Message published successfully to topic {topic}")
        else:
            print(f"Failed to publish message to topic {topic}")

# client = connect_mqtt()
# client.loop_start()
# # data = {
# #     "name":"Hello World",
# #     "Status":"Sick"
# #0 is no_helmet, 1 is else
# data = ("1")
# publish(client,data)
# client.loop_stop()