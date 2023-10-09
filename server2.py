import socket
import pickle
import json
import os
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

def start_server():
    # Initialize socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    conn, addr = server_socket.accept()

    print(f"Connection received from {addr}")

    # Receive and deserialize dictionary from client
    format = conn.recv(1).decode()  # Receive the format indicator
    data = conn.recv(1024)

    if format == "b":
        received_dict = pickle.loads(data)
    elif format == "j":
        received_dict = json.loads(data.decode('utf-8'))
    elif format == "x":
        root = ET.fromstring(data.decode('utf-8'))
        received_dict = {child.tag: child.text for child in root}

    print(f"Received dictionary: {received_dict}")

    # Receive and decrypt file data from client
    file_data = conn.recv(1024)

    # Use a preset key for decryption
    key = b'oLLcRVDpd5bqyGLlgGrMi4ARU8uoH01UNEX32hrY-Do='  # Replace with your preset key
    cipher_suite = Fernet(key)
    try:
        file_data = cipher_suite.decrypt(file_data)
        print("File data has been decrypted.")
    except:
        print("File data has not been encrypted.")

    print_option = input("Print the file data to screen? (yes/no): ")
    if print_option.lower() == "yes":
        print("File data: " + file_data.decode())

    file_option = input("Write the file data to a file? (yes/no): ")
    if file_option.lower() == "yes":
        with open('received_file.txt', 'w') as f:
            f.write(file_data.decode())

    conn.close()

if _name_ == "_main_":
    start_server()
