import subprocess

subprocess.run(["tmux", "split-window", "-h", "-t", "mqtt_session:0.1"])
subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.2",
                "mosquitto_sub -h localhost -t sensor1/motd", "C-m"])

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