import subprocess
import time

subprocess.run(["python3", "tmux.py"])







for i in range(10, 0, -1):
    time.sleep(1)


subprocess.run(["tmux", "attach", "-t", "mqtt_session"])