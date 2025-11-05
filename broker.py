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




