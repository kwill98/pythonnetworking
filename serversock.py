#!/usr/bin/python3
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET),
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
