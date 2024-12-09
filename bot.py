from telethon import TelegramClient, events
from config import api_id, api_hash, group_ids, tracked_usernames, forward_bot_username,enable_forwarding_rule
from utils.handlers import message_handler

client = TelegramClient('my_userbot', api_id, api_hash)

async def main():
    try:
        print("Bot çalışıyor, mesajları dinliyor...")

        @client.on(events.NewMessage(chats=group_ids))
        async def handler(event):
            await message_handler(event, client, tracked_usernames, forward_bot_username,enable_forwarding_rule)

        await client.run_until_disconnected()
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    client.start()
    client.loop.run_until_complete(main())
