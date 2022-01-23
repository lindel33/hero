from datetime import datetime, timedelta
from pprint import pprint
import requests
from settings import bot, chat_id, from_chat_id, API_KEY, token
from file_op import read_message_id, write_message_id, read_current_id, write_current_id


def new_current_id(list_info):
    id_now = read_current_id()

    for message in list_info:
        if message not in id_now:
            id_now.append(message)
    return id_now


def get_all_media_group_id(history_tmp, media_group):
    list_photos = []
    for post in history_tmp:
        if 'channel_post' in post:
            if 'media_group_id' in post['channel_post']:
                if post['channel_post']['media_group_id'] == media_group:
                    photo = post['channel_post']['photo'][0]['file_id']
                    list_photos.append(photo)
    return list_photos


def get_all_id_messages_updates():
    history = requests.get(API_KEY + 'getUpdates').json()
    history = history['result']
    id_list = read_message_id()
    list_info = []
    # pprint(history)
    # Все message_id в истории чата
    for post in history:
        if 'channel_post' in post:
            if 'message_id' in post['channel_post']:
                if 'caption' in post['channel_post']:
                    post_id = post['channel_post']['message_id']
                    if str(post_id) + '\n' not in id_list:
                        date = post['channel_post']['date']
                        messageTime = datetime.utcfromtimestamp(date)
                        messageTime = messageTime.strftime('%Y-%m-%d %H')
                        now_time = datetime.today()
                        re_send_time = now_time + timedelta(days=5)
                        photo_list = get_all_media_group_id(history, post['channel_post']['media_group_id'])
                        list_info.append([post_id,
                                          {
                                              'date': messageTime,
                                              'caption': post['channel_post']['caption'],
                                              'media_group_id': post['channel_post']['media_group_id'],
                                              'photo': photo_list,
                                              're_send_time':str(re_send_time.__format__('%Y-%m-%d %H')),
                                          }])

    write_message_id(list_info)
    write_current_id(new_current_id(list_info))
    return id_list

get_all_id_messages_updates()

