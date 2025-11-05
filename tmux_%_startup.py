import subprocess

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

def start_process(process_name):
    result = subprocess.run(["tmux", "send-keys", "-t", "mqtt_session:0.0", f"python3 {process_name}", "C-m"]
, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

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

start_process("broker.py")