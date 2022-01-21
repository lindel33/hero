import json
from pprint import pprint
from unittest import TestCase
from file_op import read_message_id, get_all_data, write_message_id, remove_message_id
test_text_file = 'text_files/test.txt'
test_data = [
    [290, {"date": 1642715480, "media_group_id": "13141723845887314"}],
    [293, {"date": 1642717633, "media_group_id": "13141741071605082"}],
]
test_data_remove = [
    [290, {"date": 1642715480, "media_group_id": "13141723845887314"}],
]
test_data_current = [
    
]
test_data_current_remove = [

]


class TestLoad(TestCase):
    def setUp(self) -> None:
        with open(test_text_file, 'w') as file:
            json.dump(test_data, file)

    def test_equal_data(self):
        self.assertEqual(get_all_data(test_text_file)[0][1]['media_group_id'], '13141723845887314')
        self.assertEqual(get_all_data(test_text_file)[0][1]['date'], 1642715480)
        self.assertEqual(get_all_data(test_text_file)[1][1]['media_group_id'], '13141741071605082')
        self.assertEqual(get_all_data(test_text_file)[1][1]['date'], 1642717633)

    def test_read_message_id(self):
        self.assertEqual(read_message_id(test_text_file), [290, 293])

    def test_write_message_id(self):
        self.assertEqual(write_message_id(test_data, test_text_file), True)

    def test_get_all_data(self):
        self.assertEqual(get_all_data(test_text_file), test_data)

    def test_remove_message_id(self):
        self.assertEqual(remove_message_id(293, test_text_file), True)

    def test_read_current_id(self):
        pass

    def test_write_current_id(self):
        pass
