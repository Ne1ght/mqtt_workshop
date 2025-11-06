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

def is_running(mos_part): #checks logic for the publisher and subscriber
    result = subprocess.run(["pgrep", "-f", mos_part], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def kill_process(process_name):
    result = subprocess.run(["pkill", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def start_process(process_name, pane):
    cmd = f"tmux send-keys -t mqtt_session:{pane} python3 space {process_name} enter"
    result = subprocess.run(cmd,shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("test")
    return result.returncode == 0

if is_running("mosquitto_sub"):
    print("subscriber is running")
    print("subscriber is now being stopped and restarted.")
    kill_process("mosquitto_sub")
    start_process("subscriber.py", "0.1")

else:
    print("subscriber is not running")
    start_process("subscriber.py", "0.1")


while True:
    temperatur = round(random.uniform(20.0, 30.0), 2)
    feuchtigkeit = round(random.uniform(20.0, 70.0), 2)
    daten = json.dumps({"temperatur": temperatur, "feuchtigkeit": feuchtigkeit})
    client.publish(topic, daten)
    print(f"Gesendet: {daten}")
    time.sleep(20)