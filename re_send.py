from datetime import datetime, date, timedelta
# import requests
from pprint import pprint

from telebot.types import InputMediaPhoto

from file_op import read_ready_id, write_ready_id, read_current_id
from settings import bot, chat_id, from_chat_id, API_KEY, token
# from file_op import read_message_id, write_message_id, read_current_id, write_current_id


def add_ready_id(message_id):
    ready_list = read_ready_id()
    if message_id not in ready_list:
        ready_list.append(message_id)
        write_ready_id(ready_list)


def get_message_to_send():
    exit_id = []
    current_id = read_current_id()
    today = datetime.today()
    no_send = read_ready_id()

    for message in current_id:
        if message[0] not in no_send:
            str_date = str(message[1]['re_send_time'])
            date_now = datetime.strptime(str_date, '%Y-%m-%d %H')
            if date_now < today:
                exit_id.append(message)

    return exit_id


def re_send_message():
    message = get_message_to_send()

    if message:
        for mess in message:
            if len(mess[1]['photo']) == 3:
                bot.send_media_group(chat_id=from_chat_id, media=[
                    InputMediaPhoto(media=mess[1]['photo'][0], caption=mess[1]['caption']),
                    InputMediaPhoto(media=mess[1]['photo'][1]),
                    InputMediaPhoto(media=mess[1]['photo'][2]),
                ])

            elif len(mess[1]['photo']) == 5:
                bot.send_media_group(chat_id=from_chat_id, media=[
                    InputMediaPhoto(media=mess[1]['photo'][0], caption=mess['caption']),
                    InputMediaPhoto(media=mess[1]['photo'][1]),
                    InputMediaPhoto(media=mess[1]['photo'][2]),
                    InputMediaPhoto(media=mess[1]['photo'][3]),
                    InputMediaPhoto(media=mess[1]['photo'][4]),
                ])
            else:
                print('Ошибка в кол-ве фото')
        return 0

