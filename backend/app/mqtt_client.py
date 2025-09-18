import paho.mqtt.client as mqtt
import json
from config import settings

BROKER = settings.mqtt_broker
PORT = settings.mqtt_port
TOPIC = "farm/+/device/+/telemetry"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("MQTT connected with result code ", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
    except Exception as e:
        print("Invalid MQTT payload", e)
        return
    print("Received MQTT:", payload)
    # TODO: push to scoring + DB

def start_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_start()
