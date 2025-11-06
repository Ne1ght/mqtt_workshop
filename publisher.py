import subprocess

subprocess.run(["tmux", "split-window", "-v", "-t", "mqtt_session:0.0"])
subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.1",
                'mosquitto_pub -h localhost -t sensor1/motd -m "Good morning!"', "C-m"])