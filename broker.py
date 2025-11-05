import subprocess

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

def tmux_installed(): #checks if tmux is installed
    result = subprocess.run(["which", "tmux"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def install_tmux(): #installs tmux
    installing_tmux = subprocess.run(["sudo", "apt", "install", "-y", "tmux"], capture_output=True, text=True)
    if installing_tmux.returncode != 0:
        print("tmux installation failed:", installing_tmux.stderr)
        return False
    return True

def created_tmux_session(): #starts tmux to manage the mqtt session
    result = subprocess.run(["tmux", "new-session", "-s", "mqtt_session"], capture_output=True, text=True)
    if result.returncode != 0:
        print("tmux session creation failed:", result.stderr)
        return False
    print("tmux session created successfully")
    return True

def is_running(mos_part): #checks logic for the publisher and subscriber
    result = subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.0", "pgrep", "-f", mos_part], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def kill_process(process_name):
    result = subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.0", "pkill", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def start_process(process_name):
    result = subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.0", "python3", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

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

if tmux_installed(): #calls the functions to check, install and start tmux to manage the mqtt session in ssh over one window
    print("tmux is installed")
    print("starting tmux now.")
    input("Press any key to continue and start tmux session...")
    created_tmux_session()
else:
    print("tmux is not installed!")
    print("installing tmux now.")
    if install_tmux():
        print("tmux installation successful")
        print("starting tmux now.")
        input("Press any key to continue and start tmux session...")
        created_tmux_session()
    else:
        print("tmux could not be installed! Please review code and fix.")


if is_running("mosquitto_pub"):
    print("publisher is running")
    print("publisher is now being stopped and restarted.")
    kill_process("mosquitto_pub")
    start_process("mosquitto_pub")
else:
    print("publisher is not running")
    start_process("mosquitto_pub")

if is_running("mosquitto_sub"):
    print("subscriber is running")
    print("subscriber is now being stopped and restarted.")
    kill_process("mosquitto_sub")
    start_process("mosquitto_sub")

else:
    print("subscriber is not running")
    start_process("mosquitto_sub")




