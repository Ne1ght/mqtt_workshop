import subprocess
import time

subprocess.run(["python3", "tmux.py"])




cmd = 'tmux new-session -d -s mqtt_session \; send-keys "python3 broker.py" Enter'
subprocess.run(cmd, shell=True)


for i in range(10, 0, -1):
    time.sleep(1)


subprocess.run(["tmux", "attach", "-t", "mqtt_session"])