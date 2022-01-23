from pprint import pprint

while True:
    import time
    from re_send import re_send_message
    from main import get_all_id_messages_updates
    from tmp_check import check_message_key_word, send_check_message
    all = get_all_id_messages_updates()
    pprint(all)
    for idm in all:


        tmp__id = send_check_message(idm)
        check_message_key_word(tmp__id[0], tmp__id[1], tmp__id[2])

        time.sleep(10)
