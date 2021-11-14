from telethon.sync import TelegramClient
number_of_messages = 200
messages_sent = 0
client = TelegramClient('session_name', 'api_id', 'api_hash')
client.start()
destination_group_invite_link = 'https://t.me/joinchat/wsCE5Z10fk80Mjc0'
entity = client.get_entity(destination_group_invite_link)
if messages_sent <= number_of_messages:
    client.send_message(entity=entity,message="- ++++ + +++++++ +-+ + +++- --- +-++ ++- - ++ --- -+ +++++++ ++++ +- +++ +++++++ -+++ + --+ ++- -+ -+-+--")
