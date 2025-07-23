from .models import Account

from . import utils as utl

class AccountService:
    @staticmethod
    def register(tel_number: str):
        tel_num = utl.check_number(tel_number)
        verification_code = utl.generate_verification_code()
        print(verification_code) # отправка кода
        invite_code = utl.generate_invite_code()
        acc, created = Account.objects.get_or_create(
            phone_number=tel_num,
            defaults={
                'invite_code': invite_code,
                'invite_account': None,
            },
        )
        return acc
        
