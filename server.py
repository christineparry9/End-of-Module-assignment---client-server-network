import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

def deserialize_data(data, serialization_format):
    if serialization_format == "binary":
        return pickle.loads(data)
    elif serialization_format == "json":
        return json.loads(data.decode())
    elif serialization_format == "xml":
        root = ET.fromstring(data.decode("utf-8"))
        data_dict = {}
        for element in root:
            data_dict[element.tag] = element.text
        return data_dict
    else:
        raise ValueError("Invalid serialization format")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    conn, addr = server_socket.accept()
    print(f"Connection received from {addr}")

    key = b'6WkZxGZxaFNba2sPXg8mbIgXxhjdw1iIo6DgymmqT_Q='
    cipher_suite = Fernet(key)
    file_content = b""

    try:
        serialization_format = conn.recv(1024).decode().strip()
        data = conn.recv(1024)
        received_dict = deserialize_data(data, serialization_format)
        print(f"Received dictionary in {serialization_format} format: {received_dict}")

        received_file_name = conn.recv(1024).decode().strip()
        received_file_size = int(conn.recv(1024).decode().strip())

        while received_file_size > 0:
            data = conn.recv(min(received_file_size, 1024))
            file_content += data
            received_file_size -= len(data)

        decrypted_file_content = cipher_suite.decrypt(file_content)

        with open(received_file_name, 'wb') as f:
            f.write(decrypted_file_content)

        user_input = input("Do you want to print file contents to the screen? (yes/no): ")
        if user_input.lower().strip() == 'yes' and decrypted_file_content:
            try:
                print("File content:")
                print(decrypted_file_content.decode("utf-8"))
            except UnicodeDecodeError:
                print("Cannot decode binary file to text.")
        elif not decrypted_file_content:
            print("No file content to print.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    start_server()
