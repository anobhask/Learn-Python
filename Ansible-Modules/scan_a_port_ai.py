import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    sock.close()

ip = input("Enter the IP address to scan: ")
port = int(input("Enter the port number to scan: "))
scan_port(ip, port)

