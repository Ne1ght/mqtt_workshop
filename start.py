import subprocess
import time

subprocess.run(["python3", "tmux.py"])

for i in range(10, 0, -1):
    print(f"Attaching tmux in {i} seconds")
    time.sleep(1)
subprocess.run(["tmux", "attach", "-t", "mqtt_session"])
for i in range(10, 0, -1):
    print(f"waiting to attach: {i} seconds")
    time.sleep(1)

subprocess.run([
    "tmux", "new-session", "-d", "-s", "mqtt_session",
    ";", "send-keys", "python3 broker.py", "Enter"
], shell=True)