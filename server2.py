import socket
import json

HOST = "localhost"  
PORT = 9999  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Server Started")
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                data = data.decode("utf-8")
                data = json.loads(data)
                print("received data", data)
