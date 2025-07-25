import random
import string
import asyncio
import threading

from django.core.validators import RegexValidator
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest

from config import settings as st

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефона должен быть в формате: '+999999999'. Максимум 15 цифр."
)


def check_number(tel_num: str) -> str:
    if tel_num[0] == "+":
        return tel_num
    return "+" + tel_num

def generate_invite_code() -> str:
    """Генерирует случайный инвайт-код из 6 символов"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def generate_verification_code() -> int:
    return random.randint(1000, 9999)

def create_event_loop_for_tg(phone_number: str, verification_code: int) -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sender', st.TG_API_ID, st.TG_API_HASH) as client:
        message_text = "Ваш код регистрации: " + str(verification_code)
        entity = client.get_input_entity(phone_number)
        client(SendMessageRequest(
            peer=entity,
            message=message_text,
        ))
    loop.close()

def tg_send_verification_code(phone_number: str, verification_code: int):
    thread = threading.Thread(
        target=create_event_loop_for_tg,
        args=(phone_number,verification_code,),
    )
    thread.start()
    thread.join()
