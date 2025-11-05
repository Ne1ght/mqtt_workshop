import subprocess
import time

subprocess.run(["python3", "tmux.py"])

subprocess.run(["tmux", "attach", "-t", "mqtt_session"])