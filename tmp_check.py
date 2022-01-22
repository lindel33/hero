from pprint import pprint
import requests
import self as self

from file_op import read_message_id, remove_message_id, write_message_id, write_ready_id, read_ready_id, \
    read_current_id, write_current_id
from settings import bot, chat_id, from_chat_id, API_KEY


def remove_post(message_id):
    # Удаляет из канала пост по id
    bot.delete_message(chat_id=chat_id, message_id=message_id)


def send_check_message(message_id):
    """
    Делает копию поста в tmp_канала
    :param message_id:
    :return: message_id_tmp, message_id
    """
    message_id_tmp = bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
    message_id_tmp = message_id_tmp.__dict__['message_id']
    return message_id_tmp, message_id


def check_key(post):
    """
    Проверка наличия ключей в словаре result
    :return:
    """
    if 'channel_post' in post:
        if 'message_id' in post['channel_post']:
            post_id = post['channel_post']['message_id']
            if 'caption' in post['channel_post']:
                return post_id
    return False


def check_text(text):
    pass


def check_message_key_word(message_id_tmp, message_id):
    history = requests.get(API_KEY + 'getUpdates').json()
    history = history['result']
    # pprint(history)
    list_ready_id = read_ready_id()
    list_current_id = read_current_id()
    for post in history:
        post_id = check_key(post)
        if post_id:
            if post_id == message_id:

                text = post['channel_post']['caption']
                list_text = list(text.split('\n'))
                list_text = [i for i in list_text if i != '']
                for line in list_text:
                    # print(line)
                    if 'Продано' in line:
                        if post_id in list_ready_id:
                            try:
                                list_current_id.remove(post_id)
                            except:
                                pass
                        if post_id not in list_ready_id:
                            list_ready_id.append(post_id)
                            try:
                                list_current_id.remove(post_id)
                            except:
                                pass
                        write_current_id(data=list_current_id)
                        write_ready_id(data=list_ready_id)
                        return True, message_id_tmp, message_id
                return False, message_id_tmp, message_id


# (337, 293) (339, 300) (343, 303)
x = send_check_message(309)
res = check_message_key_word(x[0], x[1])

pprint(res)

# res = check_message_key_word(339, 300)
# pprint(res)

