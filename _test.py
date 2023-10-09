
import unittest
from unittest.mock import patch, MagicMock
import pickle
import json
import xml.etree.ElementTree as ET
from client import Client

class TestClient(unittest.TestCase):
    #using unittest.mock to mock the socket
    @patch("client.socket") #The @patch("client.socket") is used to mock the socket module in client code
    def test_start_client(self, mock_socket):
        # Mocking the socket
        mock_socket_instance = MagicMock() # A mock object which is returned when socket.socket() is called in the Client class
        mock_socket.AF_INET = MagicMock() #Parameters that receive the mocked socket object.
        mock_socket.SOCK_STREAM = MagicMock()
        mock_socket.socket.return_value = mock_socket_instance# sets the return_value of socket.socket() method call to be mock_socket_instance. So when socket.socket() is called in start_client method, mock_socket_instance will be returned

        client = Client() #An instance of the Client class is created.
        client.start_client() #The start_client method of the Client instance is called. It will use the mocked socket due to @patch a few lines up

        # check if the socket methods are called correctly
        #asserts that socket.socket() was called once with mock_socket.AF_INET and mock_socket.SOCK_STREAM as arguments.
        mock_socket.socket.assert_called_once_with(mock_socket.AF_INET, mock_socket.SOCK_STREAM)
        #the connect method of the mocked socket instance (mock_socket_instance) is called once with ('localhost', 12345) as its argument, ensuring the client attempts to connect to the correct server address and port
        mock_socket_instance.connect.assert_called_once_with(('localhost', 12345))

    #tests to check if each serialization type is working
    def test_serialize_dict_binary(self):
        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        #if these 2 values are equal, the method should serialize in binary
        self.assertEqual(Client.serialize_dict(data_dict, 'binary'), pickle.dumps(data_dict))

    def test_serialize_dict_json(self):
        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        self.assertEqual(Client.serialize_dict(data_dict, 'json'), json.dumps(data_dict).encode('utf-8'))

    def test_serialize_dict_xml(self):
        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        root = ET.Element("data")
        for key, value in data_dict.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        self.assertEqual(Client.serialize_dict(data_dict, 'xml'), ET.tostring(root, encoding='utf-8'))



if __name__ == '__main__':
    unittest.main()
