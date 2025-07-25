import os

from dotenv import load_dotenv
from telethon.sync import TelegramClient

load_dotenv()

with TelegramClient('sender', os.getenv('TG_API_ID'), os.getenv('TG_API_HASH'))as client:
    client.send_message('me', 'You created session file')
