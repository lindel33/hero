
from pprint import pprint
import requests

from file_op import read_message_id, remove_message_id, write_message_id, write_ready_id, read_ready_id, \
    read_current_id, write_current_id
from re_send import get_message_to_send, re_send_message

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
    message_id_tmp = bot.forward_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
    text = message_id_tmp.caption
    message_id_tmp = message_id_tmp.__dict__['message_id']

    return message_id_tmp, message_id, text


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


def check_message_key_word(message_id_tmp, message_id, text_tmp):

    history = requests.get(API_KEY + 'getUpdates').json()
    history = history['result']

    list_ready_id = read_ready_id()
    list_current_id = read_current_id()
    for post in history:
        post_id = check_key(post)
        if post_id:
            if post_id == message_id:
                list_text = list(text_tmp.split('\n'))
                list_text = [i for i in list_text if i != '']
                for line in list_text:
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
                        bot.delete_message(chat_id=from_chat_id, message_id=post_id)

                        write_current_id(data=list_current_id)
                        write_ready_id(data=list_ready_id)
                        return True, message_id_tmp, message_id
                    re_send_message()
                return False, message_id_tmp, message_id




