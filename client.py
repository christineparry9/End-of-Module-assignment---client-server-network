import socket
import pickle
import os


def start_client():
    # Initialize socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Create and populate a dictionary
    data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}

    # Serialize the dictionary
    serialized_data = pickle.dumps(data_dict)

    # Send the serialized dictionary to the server
    client_socket.sendall(serialized_data)

    print("Dictionary has been sent")



    #get teh txt file to send
    file = open('sample_file.txt', 'rb')

    #get the sze of the txt file
    size = os.path.getsize('sample_file.txt')

    #transmit file name and size to the receiver
    # client_socket.send("received_file.txt".encode())
    # client_socket.send(str(size).encode())

    #send all data to receiver
    data = file.read()
    client_socket.sendall(data)

    print("File has been sent.")

    client_socket.close()

        # Create and populate a text file
    # with open('sample_file.txt', 'w') as f:
    #     f.write('Hello, this is a sample file content.')


    # Read and send the text file
    # with open('sample_file.txt', 'rb') as f:
    #     while True:
    #         file_data = f.read(1024)
    #         if not file_data:
    #             break
    #         client_socket.sendall(file_data)

if __name__ == "__main__":
    start_client()
# test line