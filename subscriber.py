import subprocess

subprocess.run(["tmux", "split-window", "-h", "-t", "mqtt_session"])
subprocess.run(["mosquitto_sub", "-h", "localhost", "sensor1/motd"])