import socket
import pickle
import os
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Function to serialize dictionary based on format
def serialize_dict(data_dict, serialization_format):
    if serialization_format == "binary":
        return pickle.dumps(data_dict)
    elif serialization_format == "json":
        return json.dumps(data_dict).encode()
    elif serialization_format == "xml":
        root = ET.Element("data")
        for key, value in data_dict.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        return ET.tostring(root)
    else:
        raise ValueError("Invalid serialization format")

def start_client():
    # Initialize socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Create and populate a dictionary
    data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}

    # User can set pickling format to binary, JSON, or XML
    serialization_format = input("Enter serialization format (binary/json/xml): ").lower()

    try:
        # Serialize the dictionary based on user's choice
        serialized_data = serialize_dict(data_dict, serialization_format)

        # Send the serialized dictionary to the server
        client_socket.sendall(serialized_data)
        print(f"Dictionary has been sent in {serialization_format} format")

        # Get the text file to send
        file = open('sample_file.txt', 'rb')

        # Get the size of the text file
        size = os.path.getsize('sample_file.txt')

        # Transmit file name and size to the receiver
        client_socket.send("received_file.txt".encode())
        client_socket.send(str(size).encode())

        # Send all data to receiver
        data = file.read()
        client_socket.sendall(data)

        print("File has been sent.")

        client_socket.close()

    except ValueError as e:
        print(f"Error: {e}")
        client_socket.close()

if __name__ == "__main__":
    start_client()
