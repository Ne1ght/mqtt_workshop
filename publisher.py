import subprocess
import paho.mqtt.client as mqtt
import time
import random
import json

subprocess.run(["tmux", "split-window", "-v", "-t", "mqtt_session:0.0"])
subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.1",
                'mosquitto_pub -h localhost -t sensor1/motd -m "Good morning!"', "C-m"])

broker = "localhost"
topic = "demo/sensor/temp_feuchte"

client = mqtt.Client()
client.connect(broker, 1883, 60)


while True:
    temperatur = round(random.uniform(20.0, 30.0), 2)
    feuchtigkeit = round(random.uniform(20.0, 70.0), 2)
    daten = json.dumps({"temperatur": temperatur, "feuchtigkeit": feuchtigkeit})
    client.publish(topic, daten)
    print(f"Gesendet: {daten}")
    time.sleep(20)