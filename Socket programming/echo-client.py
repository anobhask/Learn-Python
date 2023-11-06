# echo-client.py

import socket
import argparse
import pickle 

parser = argparse.ArgumentParser()
parser.add_argument("-n","--name",help="Employee name",type=str,default="Anoop KB")
parser.add_argument("-m","--mail",help="Employee e-mail",type=str,default="Anoop@hcl.com")
parser.add_argument("-b","--band",help="Employee band",type=int,default=1)
args = parser.parse_args()

my_data = {
    "Name":"Anoop",
    "Job":"devOps"
}

emp_data = {
    "emp_name":args.name,
    "emp_mail":args.mail,
    "emp_band":args.band
}

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall((pickle.dumps(emp_data)))
    data = s.recv(1024)

print(f"Received {data!r}")