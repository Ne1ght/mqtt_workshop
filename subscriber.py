import subprocess
import paho.mqtt.client as mqtt
import json

subprocess.run(["tmux", "split-window", "-h", "-t", "mqtt_session:0.1"])
subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.2",
                "mosquitto_sub -h localhost -t sensor1/motd", "C-m"])

broker = "mqtt.eclipseprojects.io"
topic = "demo/sensor/temp_feuchte"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbunden zum Broker")
        client.subscribe(topic)
    else:
        print("Verbindungsfehler:", rc)

def on_message(client, userdata, msg):
    daten = json.loads(msg.payload.decode())
    print(f"Empfangen - Temperatur: {daten['teemperatur']}°C, Feuchtigkeit: {daten['feuchtigkeit']}%")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()