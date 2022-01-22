from pprint import pprint
import requests
from settings import bot, chat_id, from_chat_id, API_KEY, token
from file_op import read_message_id, write_message_id, read_current_id, write_current_id

history = requests.get(API_KEY + 'getUpdates').json()
history = history['result']


def new_current_id(list_info):
    try:
        id_now = read_current_id()
        for message in list_info:
            if message[0] not in id_now:
                id_now.append(message[0])
        return id_now
    except:
        pass


def get_all_id_messages_updates():
    id_list = read_message_id()
    list_info = []
    # Все message_id в истории чата
    for post in history:
        if 'channel_post' in post:
            if 'message_id' in post['channel_post']:
                if 'caption' in post['channel_post']:
                    post_id = post['channel_post']['message_id']
                    if str(post_id) + '\n' not in id_list:
                        list_info.append([post_id,
                                          {
                                              'date': post['channel_post']['date'],
                                              'media_group_id': post['channel_post']['media_group_id'],
                                          }])

    write_message_id(list_info)
    write_current_id(new_current_id(list_info))
    return id_list

pprint(get_all_id_messages_updates())

