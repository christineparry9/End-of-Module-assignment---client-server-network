# Python Socket Communication

This repository contains a basic application demonstrating client-server communication using Python sockets, involving sending a serialized dictionary and a file from the client to the server.

## How It Works

### Client

1. **Serialization of Data**:
   - The client serializes a predefined dictionary into a format specified by the user (options: `binary`, `json`, or `xml`).
2. **File Transfer**:
   - The client sends a file (name and content) to the server.
3. **Communication**:
   - All data is communicated through TCP/IP using sockets.

### Server

1. **Deserialization of Data**:
   - The server receives the data, identifying and deserializing it based on the specified format.
2. **File Reception**:
   - The server receives, decodes (if possible), and stores the file.
3. **User Interaction**:
   - Provides an option to print the received file's content to the console.

## Prerequisites

- Python 3.x
- Basic understanding of socket programming.

## How to Use

### Client

1. **Run**: Execute `client.py`.
2. **Input**: Provide the desired serialization format (`binary`, `json`, or `xml`) when prompted.
3. **Observe**: Note that the client sends a predefined dictionary and file to the server.

### Server

1. **Run**: Execute `server.py` to initiate the server.
2. **Receive**: The server will automatically handle incoming connections, receiving, and deserializing the data, outputting the dictionary to the console.
3. **Interact**: The user is provided an option to print the file content to the console, following a prompt.

## Files

### client.py

- Initializes and connects the client socket to the server.
- Serializes and sends a predefined dictionary and file to the server.

### server.py

- Initializes the server socket, awaiting client connection.
- Upon connection, receives and deserializes the dictionary, and outputs it to the console.
- Receives a file, saves it, and (if desired) displays the content in the console upon user request.

## Error Handling

- Both scripts are equipped to handle `ValueError` which could occur during (de)serialization processes.

## Note

- Ensure that the server script is running before starting the client script, and that they are operating on the same network and port.
