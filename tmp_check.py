from pprint import pprint
import requests
from file_op import read_message_id, remove_message_id, write_message_id, write_ready_id
from settings import bot, chat_id, from_chat_id, API_KEY


def remove_post(message_id):
    # Удаляет из data.txt id поста товара если он продан
    # Удаляет из канала пост по id
    bot.delete_message(chat_id=chat_id, message_id=message_id)
    remove_message_id(message_id)


def send_check_message(message_id):
    """
    Делает копию поста в tmp_канала
    :param message_id:
    :return: message_id_tmp, message_id
    """
    message_id_tmp = bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
    message_id_tmp = message_id_tmp.__dict__['message_id']
    return message_id_tmp, message_id


def check_message_key_word(message_id_tmp, message_id):
    history = requests.get(API_KEY + 'getUpdates').json()
    history = history['result']
    for post in history:
        if 'channel_post' in post:
            if 'message_id' in post['channel_post']:
                post_id = post['channel_post']['message_id']
                if 'caption' in post['channel_post']:
                    if post_id == message_id_tmp:
                        text = post['channel_post']['caption']
                        list_text = list(text.split('\n'))
                        list_text = [i for i in list_text if i != '']
                        for line in list_text:
                            if 'Продано' in line:
                                write_ready_id(data=post_id)
                                return True, message_id
                        return False, message_id_tmp
