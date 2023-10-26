import os

from telethon import TelegramClient, events
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

APP_ID = os.getenv("APP_ID", default=None)
API_HASH = os.getenv("API_HASH", default=None)
FROM_ = os.getenv("FROM_CHANNEL")
TO_ = os.getenv("TO_CHANNEL")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

BotzHubUser.start()
@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i, source in enumerate(FROM):
        if event.chat_id == source:
            destination = TO[i]

            try:
                BotzHubUser = TelegramClient('session', APP_ID, API_HASH)

            except Exception as ap:
                print(f"ERROR - {ap}")
                exit(1)
            await BotzHubUser.send_message(
                destination,
                event.message
            )
            break

    print(i+1)


print("Bot has started.")
BotzHubUser.run_until_disconnected()
