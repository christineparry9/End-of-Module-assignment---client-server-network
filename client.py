import socket
import pickle
import os
import json
import xml.etree.ElementTree as ET


class Client:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port

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
            # Ensure XML is encoded to bytes before sending
            return ET.tostring(root, encoding="utf-8")
        else:
            raise ValueError("Invalid serialization format")

    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))

        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}

        serialization_format = input("Enter serialization format (binary/json/xml): ").lower()

        try:
            serialized_data = Client.serialize_dict(data_dict, serialization_format)
             # Send the serialized dictionary to the server
            client_socket.sendall(serialization_format.ljust(1024).encode())
            client_socket.sendall(serialized_data)
            print(f"Dictionary has been sent in {serialization_format} format")

            # Transmit file name and size to the receiver
            file_name = 'example.txt'
            file_size = os.path.getsize(file_name)

            client_socket.sendall(file_name.ljust(1024).encode())
            client_socket.sendall(str(file_size).ljust(1024).encode())

            # Send file data to the receiver
            with open(file_name, 'rb') as file:
                client_socket.sendall(file.read())

            print("File has been sent.")

        except ValueError as e:
            print(f"Error: {e}")

        finally:
            client_socket.close()

if __name__ == "__main__":
    client_instance = Client()
    client_instance.start_client()
