import subprocess

subprocess.run(["tmux", "split-window", "-v", "-t", "mqtt_session"])
subprocess.run(["mosquitto_pub", "-h", "localhost", "-t", "sensor1/motd", "-m", "Good morning!"])