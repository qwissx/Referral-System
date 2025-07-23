import random
import string

from django.core.validators import RegexValidator


def check_number(tel_num: str) -> str:
    if tel_num[0] == "+":
        return tel_num
    return "+" + tel_num

def generate_invite_code() -> str:
    """Генерирует случайный инвайт-код из 6 символов"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def generate_verification_code() -> int:
    return random.randint(1000, 9999)

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефона должен быть в формате: '+999999999'. Максимум 15 цифр."
)
