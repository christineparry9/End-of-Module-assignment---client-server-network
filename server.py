import socket
import pickle
import json
import xml.etree.ElementTree as ET

# Function to deserialize based on format
def deserialize_data(data, serialization_format):
    if serialization_format == "binary":
        return pickle.loads(data)
    elif serialization_format == "json":
        return json.loads(data.decode())
    elif serialization_format == "xml":
        # Ensure data is decoded to a string before parsing as XML
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

    try:
        # Receive the serialization format from the client
        serialization_format = conn.recv(1024).decode().strip()

        # Receive and deserialize dictionary from client
        data = conn.recv(1024)
        received_dict = deserialize_data(data, serialization_format)
        print(f"Received dictionary in {serialization_format} format: {received_dict}")

        # Receive file name and size
        received_file_name = conn.recv(1024).decode().strip()
        received_file_size = int(conn.recv(1024).decode().strip())

        # Initialize a bytes variable to store the file content in case we want to print it
        file_content = b""

        # Receive and handle text file
        with open(received_file_name, 'wb') as f:
            while received_file_size > 0:
                data = conn.recv(min(received_file_size, 1024))
                print(f"Received chunk size: {len(data)} bytes")  # Debugging line
                f.write(data)
                file_content += data
                received_file_size -= len(data)

        print("File has been received.")


        # Ask the user if they want to print the file content
        user_input = input("Do you want to print file contents to the screen? (yes/no): ")
        if user_input.lower().strip() == 'yes' and file_content:
            try:
                # Attempt to decode and print the file content
                print("File content:")
                print(file_content.decode("utf-8"))
            except UnicodeDecodeError:
                print("Cannot decode binary file to text.")
        elif not file_content:
            print("No file content to print.")




    except ValueError as e:
        print(f"Error: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    start_server()
