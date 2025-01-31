import socket

def get_ip():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = None
    return ip_address