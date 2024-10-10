import subprocess

def connect_vpn(server_id):
    """Connect to ProtonVPN using a specific server"""
    try:
        print(f"Connecting to ProtonVPN server: {server_id}...")
        subprocess.run(["sudo", "protonvpn-cli", "connect", server_id], check=True)
        print("Connected to VPN.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to VPN: {e}")

def disconnect_vpn():
    """Disconnect from ProtonVPN"""
    try:
        print("Disconnecting from ProtonVPN...")
        subprocess.run(["sudo", "protonvpn-cli", "disconnect"], check=True)
        print("VPN disconnected.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to disconnect VPN: {e}")


server_id = "US-FREE#1"

connect_vpn(server_id)

disconnect_vpn()