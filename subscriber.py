import subprocess
import paho.mqtt.client as mqtt
import json

broker = "localhost"
topic = "demo/sensor/temp_feuchte"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbunden zum Broker")
        client.subscribe(topic)
    else:
        print("Verbindungsfehler:", rc)

def on_message(client, userdata, msg):
    daten = json.loads(msg.payload.decode())
    print(f"Empfangen - Temperatur: {daten['temperatur']}°C, Feuchtigkeit: {daten['feuchtigkeit']}%")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()