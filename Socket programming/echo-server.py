# echo-server.py

import socket
import pickle

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

ack_data = "Received data"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if data:
                    serv_data = pickle.loads(data)
                    print(serv_data)
                if not data:
                    break
                conn.sendall(ack_data.encode("ascii"))