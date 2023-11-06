import threading
import socket
import argparse
import time
import logging
import pickle

stream_data = False
## Get current employee data from input
def get_arguents() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--name",help="Employee name",type=str,default="Anoop KB")
    parser.add_argument("-m","--mail",help="Employee e-mail",type=str,default="Anoop@hcl.com")
    parser.add_argument("-b","--band",help="Employee band",type=int,default=1)
    args = parser.parse_args()

    print(f'Name:{args.name}')
    print(f'E-mail:{args.mail}')
    print(f'Band:{args.band}')

    return {
        "emp_name":args.name,
        "emp_mail":args.mail,
        "emp_band":args.band
        }
def start_server() -> None:
    global stream_data
    local_host="127.0.0.1"
    local_port = 65432

    try:
        read_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        read_socket.bind((local_host, local_port))
        read_socket.listen()
        while True:
            local_conn, local_addr = read_socket.accept()
            print(F"Connected by {local_addr}")
            data = local_conn.recv(1024)
            if not data:
                local_conn.sendall(b'No data')
                continue
            global data_available
            stream_data = True
            data = pickle.loads(data)
            print(f"Received {data}")
            local_conn.sendall(b'ACK')
            local_conn.close()
    except KeyboardInterrupt as kb:
        exit
def write_data() -> None:
    global stream_data
    data_count = 1
    while True:
        if stream_data:
            print(f"Data availble- count : {data_count} ")
            data_count+=1
            stream_data = False
def connect_db() -> int:
    pass

def write_emp_data(emp_data) -> int:
    pass

if __name__ == "__main__":
    emp_data = get_arguents()
    print(emp_data)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main  : before creating thread")

    read_thread = threading.Thread(target=start_server)
    write_thread = threading.Thread(target=write_data)
    logging.info("Main  : before running thread")
    read_thread.start()
    logging.info("Main : Wait for READ thread to finish")
    write_thread.start()
    logging.info("Main : Wait for WRITE thread to finish")
    logging.info("Main  :all done")