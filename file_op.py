import json
from pprint import pprint
name_data_file = 'text_files/data.txt'
name_current_file = 'text_files/current.txt'
name_ready_file = 'text_files/ready_post.txt'


def get_all_data(filename=name_data_file):
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    except:
        return []


def write_message_id(data, filename=name_data_file):
    try:
        with open(filename, 'w') as file_w:
            json.dump(data, file_w)
        return True
    except:
        return False


def remove_message_id(message_id, filename=name_data_file):
    try:
        list_id = get_all_data()
        for data in list_id:
            if data[0] == message_id:
                list_id.remove(data)
        return write_message_id(data=list_id, filename=filename)
    except:
        return False


def read_current_id(filename=name_current_file):
    list_id = []
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for ids in data:
                list_id.append(ids)
        return list_id
    except:
        return []


def write_current_id(data, filename=name_current_file):
    try:
        with open(filename, 'w') as file_w:
            json.dump(data, file_w)
        return True
    except:
        return False


def read_ready_id(filename=name_ready_file):
    list_id = []
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for ids in data:
                list_id.append(ids)
        return list_id
    except:
        return []


def write_ready_id(data, filename=name_ready_file):
    try:
        with open(filename, 'w') as file_w:
            json.dump(data, file_w)
        return True
    except:
        return False


def read_message_id(filename=name_data_file):
    post_id_list = []
    with open(filename) as json_file:
        try:
            data = json.load(json_file)
            current_id = read_current_id()
            ready_id = read_ready_id()
            for id_message in data:
                if id_message[0] not in current_id[0]:
                    if id_message[0] not in ready_id:
                        post_id_list.append(id_message[0])
        except:
            print('except')
    return post_id_list

