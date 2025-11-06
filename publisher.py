import subprocess

subprocess.run(["tmux", "split-window", "-v", "-t", "mqtt_session:0.0"])
cmd = "tmux send-keys -t mqtt_workshop:0.1  mosquitto_pub -h localhost -t sensor1/motd -m Good space Mornin! C-m enter"
subprocess.run(cmd, shell=True, capture_output=True)