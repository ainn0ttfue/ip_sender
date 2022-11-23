import socket
import time
import requests
import sys

script, host, port = sys.argv
last_ip = ''


def get_ip():
    req = requests.get('http://ipinfo.io/ip')
    return req.text


def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, int(port)))
        s.sendall(str.encode(data))

        answer = s.recv(1024)
        print(f"Server answer: {answer.decode('utf-8')}")


while True:
    ip = get_ip()
    if last_ip != ip:
        print(f'New IP address: {ip}')
        last_ip = ip
        send_data(ip)

    time.sleep(1800)  # 30 minutes
