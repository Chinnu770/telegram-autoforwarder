#new posts
async def sender_bH(event):
    for i, source in enumerate(FROM):
        if event.chat_id == source:
            destination = TO[i]    #if needed can be edited to post to only one channel
            await BotzHubUser.send_message(
                destination,
                event.message
            )
            break

#existing posts
for message in messages:
        if message.date.timestamp() >= date:
            if message.message:
                client.send_message(target_channel_username, message.message)
                time.sleep(60)
            if message.media:
                client.send_file(target_channel_username, message.media, caption=message.text)
                time.sleep(60)
