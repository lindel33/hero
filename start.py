import time


while True:
    from main import get_all_id_messages_updates
    from tmp_check import check_message_key_word, send_check_message
    for idm in get_all_id_messages_updates():
        tmp__id = send_check_message(idm)
        check_message_key_word(tmp__id[0], tmp__id[1])
        time.sleep(3)
