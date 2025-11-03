import subprocess

def broker_active():
    result = subprocess.run(
        ["systemctl", "is-active", "mosquitto"]
    )
    return result.returncode == 0

if broker_active():
    print("broker is running")
else:
    print("broker is not running")