from telethon import events
from utils.logger import log_message
import re

async def message_handler(event, client, tracked_usernames, forward_bot_username,enable_forwarding_rule):
    sender = await event.get_sender()
    sender_username = sender.username or "Yok"

    if sender_username in tracked_usernames:
        log_message(f"Takip edilen kullanıcı mesaj gönderdi: @{sender_username}")
        log_message(f"Mesaj: {event.text}")
        contract_address_pattern = r'\b(0x[a-fA-F0-9]{40}|[1-9A-HJ-NP-Za-km-z]{16,64})\b'
        match = re.search(contract_address_pattern, event.text)
        if bool(match)==enable_forwarding_rule:
            try:
                await client.forward_messages(forward_bot_username, event.message)
                log_message(f"Mesaj {forward_bot_username} botuna forward edildi.")
            except Exception as e:
                log_message(f"Mesaj forward edilirken hata oluştu: {e}")
        else:
            try:
                await client.forward_messages(forward_bot_username, event.message)
                log_message(f"Mesaj {forward_bot_username} botuna forward edildi.")
            except Exception as e:
                log_message(f"Mesaj forward edilirken hata oluştu: {e}")
