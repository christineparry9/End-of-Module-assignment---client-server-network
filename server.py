import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Function to deserialize based on format
def deserialize_data(data, serialization_format):
    if serialization_format == "binary":
        return pickle.loads(data)
    elif serialization_format == "json":
        return json.loads(data.decode())
    elif serialization_format == "xml":
        root = ET.fromstring(data)
        data_dict = {}
        for element in root:
            data_dict[element.tag] = element.text
        return data_dict
    else:
        raise ValueError("Invalid serialization format")

def start_server():
    # Initialize socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    conn, addr = server_socket.accept()

    print(f"Connection received from {addr}")

    try:
        # Receive the serialization format from the client
        serialization_format = conn.recv(1024).decode()

        # Receive and deserialize dictionary from client
        data = conn.recv(1024)
        received_dict = deserialize_data(data, serialization_format)
        print(f"Received dictionary in {serialization_format} format: {received_dict}")

        # Receive file name and size
        received_file_name = conn.recv(1024).decode()
        received_file_size = int(conn.recv(1024).decode())

        # Receive and handle encrypted text file
        with open(received_file_name, 'wb') as f:
            while received_file_size > 0:
                data = conn.recv(1024)
                f.write(data)
                received_file_size -= len(data)

        print("File has been received.")

        conn.close()

    except ValueError as e:
        print(f"Error: {e}")
        conn.close()

if __name__ == "__main__":
    start_server()
