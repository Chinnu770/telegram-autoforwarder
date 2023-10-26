from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetMessagesViewsRequest

from telethon.tl.types import InputMessagesFilterPhotos

bot_token = ''
api_id = ''
api_hash = ''
username = ''
source_channel_username = 123
target_channel_username = 123


with TelegramClient(username, api_id, api_hash) as client:
    source_channel = client.get_entity(source_channel_username)

    messages = client.get_messages(source_channel, limit=None)
    for message in messages:
        if message.message:
            client.send_message(target_channel_username, message.message)
        if message.media:
            client.send_file(target_channel_username, message.media, caption=message.text)

print('Msgs sent to another channel successfully.')
