import subprocess

def broker_installed():
    result = subprocess.run(["mosquitto", "-h"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def install_broker():
    install_mosquitto = subprocess.run(["sudo", "apt", "install", "-y", "mosquitto"], capture_output=True, text=True)
    if install_mosquitto.returncode != 0:
        print("mosquitto installation failed:", install_mosquitto.stderr)
        return False
    install_client = subprocess.run(["sudo", "apt", "install", "-y" "mosquitto-clients"], capture_output=True, text=True)
    if install_client.returncode != 0:
        print("Client installation failed:", install_client.stderr)
        return False
    return True

def broker_active():
    result = subprocess.run(
        ["systemctl", "is-active", "mosquitto"]
    )
    return result.returncode == 0

if broker_installed():
    print("broker is installed")
else:
    print("broker is not installed")
    if input("Do you want to install it? (yes/no) ").strip().lower() == "yes":
        if install_broker():
            print("Broker and client installed successfully")
        else:
            print("installation failed")
            exit(1)


if broker_active():
    print("broker is running")
else:
    print("broker is not running")


