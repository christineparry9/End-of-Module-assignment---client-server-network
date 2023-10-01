import socket
import json
import os

class Client:

    def __init__(self):
        # Initialize socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client_socket.connect((host, port))

    def connect_to_server(self, host, port):
        try:    
            self.client_socket.connect((host, port))
        except:
            return "not connected"
        return "connected"

    def send_dictionary(self, data_dict):
        # Create and populate a dictionary
        #data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}

        # Serialize the dictionary
        data = json.dumps(data_dict)
        data = data.encode("utf-8")

        # Send the serialized dictionary to the server
        try:
            self.client_socket.sendall(data)

            print("Dictionary has been sent")
        except:
            return False
        
        return True

    def send_file(self, file_path):

        #get teh txt file to send
        file = open(file_path, 'rb')

        #get the sze of the txt file
        size = os.path.getsize(file_path)

        #transmit file name and size to the receiver
        # client_socket.send("received_file.txt".encode())
        # client_socket.send(str(size).encode())

        #send all data to receiver
        data = file.read()
        self.client_socket.sendall(data)

        print("File has been sent.")
        return True
    #    client_socket.close()

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

#if __name__ == "__main__":
#    client1 = start_client('localhost', 99999)
#    data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
#    result1 = send_dictionary(client1, data_dict)
#    result2 = send_file(client1, "sample_file.txt")