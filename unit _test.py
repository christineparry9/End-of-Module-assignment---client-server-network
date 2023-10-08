import unittest
from client import Client

#from client import start_client
class test_client(unittest.TestCase):

    def test_connect_to_server(self):
        test_client = Client()
        actual_output = test_client.connect_to_server("localhost", 9999)
        expected_output = "connected"
        self.assertEqual(actual_output, expected_output)

    def test_connect_to_server2(self):
        test_client = Client()
        actual_output = test_client.connect_to_server("localhost", 9999)
        expected_output = "not connected"
        self.assertEqual(actual_output, expected_output)

    def test_send_dictionary(self):
        test_client = Client()
        print(test_client.connect_to_server("localhost", 9999))
        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        actual_output = test_client.send_dictionary(data_dict)
        self.assertTrue(actual_output)

    def test_send_dictionary2(self):
        test_client = Client()
        print(test_client.connect_to_server("localhost", 1999))
        data_dict = {'name': 'Christine', 'age': 35, 'city': 'London'}
        actual_output = test_client.send_dictionary(data_dict)
        self.assertFalse(actual_output)  

if __name__=='__main__': 
    unittest.main()