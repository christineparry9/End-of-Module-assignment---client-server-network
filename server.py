import socket
import pickle


def start_server():
    # Initialize socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    conn, addr = server_socket.accept()

    print(f"Connection received from {addr}")

    # Receive and deserialize dictionary from client
    data = conn.recv(1024)
    received_dict = pickle.loads(data)
    print(f"Received dictionary: {received_dict}")

    #print contents of txt file
    file_data = conn.recv(1024).decode()
    print("file data: " + file_data)


    # Open text file for reading the received content - server only needs to know that it is a txt file
    # with open('received_file.txt', 'rb') as f:
    #     content = f.read()
    #     print(f"File content:\n{content}")
    # print("File has been received.")

    conn.close()


if __name__ == "__main__":
    start_server()
