Python Socket Communication
This application establishes a basic client-server communication using Python socket programming. The client sends a serialized dictionary and a file to the server, which then deserializes the data and saves the received file.

How It Works
Client
Serialization of Data: The client allows choosing a serialization format (binary, json, or xml) for transmitting dictionaries.
File Transfer: The client sends a file name and its content to the server.
Communication: Data is sent over TCP/IP using sockets.
Server
Deserialization of Data: The server receives data and deserializes it based on the specified format.
File Reception: The server receives, decodes (if possible), and saves the file.
User Interaction: The user has the option to print the received file content to the screen.
Prerequisites
Python 3.x
Basic knowledge of socket programming
How to Use
Client
Run client.py.
When prompted, input the desired serialization format (binary, json, or xml).
Observe the client sending data and a file to the server.
Server
Run server.py to start the server.
The server waits for a connection, receives, and deserializes the dictionary.
The server receives a file, saves it, and optionally displays its content based on user input.
Files
client.py
Initializes client socket and connects to the server.
Serializes a predefined dictionary using the chosen format.
Sends the serialized dictionary and a predefined file to the server.
server.py
Initializes server socket and waits for a connection.
Receives and deserializes the dictionary and prints it to the console.
Receives a file, saves it locally, and optionally prints its content to the console based on user input.
Error Handling
Both scripts handle ValueError which might occur during (de)serialization processes.

Note
Ensure that both scripts are running in the same network and port. The server should be started before the client.
