import subprocess
import time


def broker_installed(): #checks if mosqutitto is installed or not
    result = subprocess.run(["which", "mosquitto"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def install_broker(): #installs mosquitto and the mosquitto-client then checks if the installation was succesful
    install_mosquitto = subprocess.run(["sudo", "apt", "install", "-y", "mosquitto"], capture_output=True, text=True)
    if install_mosquitto.returncode != 0:
        print("mosquitto installation failed:", install_mosquitto.stderr)
        return False

    install_client = subprocess.run(["sudo", "apt", "install", "-y", "mosquitto-clients"], capture_output=True, text=True)
    if install_client.returncode != 0:
        print("Client installation failed:", install_client.stderr)
        return False
    return True

def broker_active(): #checks if the broker is running
    result = subprocess.run(
        ["systemctl", "is-active", "mosquitto"]
    )
    return result.returncode == 0



def is_running(mos_part): #checks logic for the publisher and subscriber
    result = subprocess.run(["pgrep", "-f", mos_part], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def kill_process(process_name):
    result = subprocess.run(["pkill", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def start_process(process_name):
    result = subprocess.run(["python3", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

subprocess.run(["tmux", "attach", "-t", "mqtt_session"])

for i in range(10, 0, -1):
    print(f"Attaching tmux in {i} seconds")
    time.sleep(1)



if broker_installed(): #calls the functions to check if the broker is installed and if not installs it
    print("broker is installed")
else:
    print("broker is not installed")
    if input("Do you want to install it? (yes/no) ").strip().lower() == "yes":
        if install_broker():
            print("Broker and client installed successfully")
        else:
            print("installation failed")
            exit(1)

if broker_active(): #calls the function to check if the broker is active
    print("broker is running")
else:
    print("broker is not running")

if is_running("mosquitto_pub"):
    print("publisher is running")
    print("publisher is now being stopped and restarted.")
    kill_process("mosquitto_pub")
    start_process("publisher.py")
else:
    print("publisher is not running")
    start_process("mosquitto_pub")

if is_running("mosquitto_sub"):
    print("subscriber is running")
    print("subscriber is now being stopped and restarted.")
    kill_process("mosquitto_sub")
    start_process("subscriber.py")

else:
    print("subscriber is not running")
    start_process("mosquitto_sub")




