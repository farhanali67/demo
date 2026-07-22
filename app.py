import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

def get_internal_ip():
    """Fetches the actual internal IP address used to connect to the internet."""
    try:
        # Create a dummy socket connection to find the interface routing traffic
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        # Fallback if there is no active internet connection interface
        return socket.gethostbyname(socket.gethostname())

@app.route('/')
def get_system_info():
    # Gather system specs and environment configurations
    system_data = {
        "hostname": socket.gethostname(),
        "ip_address": get_internal_ip(),
        "environment_variables": dict(os.environ) # Converts system env vars to a dict
    }
    return jsonify(system_data)

if __name__ == '__main__':
    # Runs the application on all available network interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)
