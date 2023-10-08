# End-of-Module-assignment---client-server-network
\# Client-Server Network Application

This application demonstrates a basic implementation of a client-server
network where a client sends serialized and optionally encrypted data to
a server using sockets in Python.

\## Description

\### Client

\- The client collects user information into a Python dictionary, then
serializes it using the user\'s preferred format (binary using pickle,
JSON, or XML). - The client also sends a .txt file, with the option to
encrypt it using the Fernet symmetric encryption.

\### Server

\- The server receives and deserializes the dictionary using the
appropriate method depending on the format specified by the client. -
The server also receives the file data, attempts to decrypt it with a
preset key, and then either displays it to the console or writes it to a
file, based on user input.

\## Setup and Run

\### Requirements

\- Python 3.x - cryptography library

Before running the scripts, make sure to install the necessary library
specified in \`requirements.txt\`.

\### Running the Scripts

1\. \*\*Server\*\*: Run \`server.py\` to start the server, which will
wait for a connection from the client. 2. \*\*Client\*\*: Run
\`client.py\` and follow the prompts to send data to the server.

\### Notes

\- Ensure that both scripts are run in environments where the necessary
Python version and libraries (as specified in \`requirements.txt\`) are
available. - Run server before client to ensure the connection can be
established. - Always ensure that the server and client are using the
same encryption key if using the encryption option. - The sample text
file (\`sample_file.txt\`) must be in the same directory as the client
script.
