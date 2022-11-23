import socket
import sys
from datetime import datetime

script, host, port = sys.argv

# todo: получать ip сервера автоматически


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, int(port)))
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                with open('ip_list.txt', 'a') as f:
                    now = datetime.now()
                    f.write(f'{now}: {data.decode("utf-8")} \n')
                conn.sendall(b'Success')
