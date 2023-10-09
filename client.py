import socket
import pickle
import os
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

class Client:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port

    @staticmethod
    def serialize_dict(data_dict, serialization_format):
        if serialization_format == "binary":
            return pickle.dumps(data_dict)
        elif serialization_format == "json":
            return json.dumps(data_dict).encode("utf-8")
        elif serialization_format == "xml":
            root = ET.Element("data")
            for key, value in data_dict.items():
                element = ET.SubElement(root, key)
                element.text = str(value)
            return ET.tostring(root, encoding="utf-8")
        else:
            raise ValueError("Invalid serialization format")

    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))

        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        serialization_format = input("Enter serialization format (binary/json/xml): ").lower()

        # Use a pre-shared key for Fernet encryption
        key = b'6WkZxGZxaFNba2sPXg8mbIgXxhjdw1iIo6DgymmqT_Q='
        cipher_suite = Fernet(key)

        try:
            serialized_data = Client.serialize_dict(data_dict, serialization_format)
            client_socket.sendall(serialization_format.ljust(1024).encode())
            client_socket.sendall(serialized_data)

            file_name = 'example.txt'

            # Encrypt the file
            with open(file_name, 'rb') as file:
                encrypted_file_data = cipher_suite.encrypt(file.read())
            print("encrypting txt file to send...")
            encrypted_file_size = len(encrypted_file_data)

            client_socket.sendall(file_name.ljust(1024).encode())
            client_socket.sendall(str(encrypted_file_size).ljust(1024).encode())
            client_socket.sendall(encrypted_file_data)

            print("sent encrypted txt file")

        except ValueError as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    client_instance = Client()
    client_instance.start_client()
