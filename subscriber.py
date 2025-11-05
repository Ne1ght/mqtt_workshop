import subprocess

subprocess.run(["tmux", "split-window", "-h", "-t", "mqtt_session"])
subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.1", "mosquitto_sub", "-h", "localhost", "sensor1/motd", "C-m"])