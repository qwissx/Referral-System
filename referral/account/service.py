from django.http import Http404

from .models import Account
from . import utils as utl


class AccountService:
    @staticmethod
    def send_code(tel_number: str):
        tel_num = utl.check_number(tel_number)
        verification_code = utl.generate_verification_code()
        account, created = Account.objects.get_or_create(
            phone_number=tel_num,
            defaults={
                'invite_code': None,
                'invite_account': None,
            },
        )
        account.register_code = verification_code
        utl.tg_send_verification_code(tel_num, verification_code)
        account.save()
        return 'Success'
       

    @classmethod
    def verify_code(cls, verification_code: int):
        account = cls.get_account_or_404(register_code=verification_code)
        invite_code = utl.generate_invite_code()
        account.invite_code = invite_code
        account.register_code = None
        account.save()
        return account
        

    @staticmethod
    def get_account_or_404(**kwargs):
        if kwargs.get("phone_number"):
            kwargs["phone_number"] = utl.check_number(kwargs.get("phone_number"))
        try:
            account = Account.objects.get(**kwargs) 
            return account
        except Account.DoesNotExist:
            raise Http404


    @classmethod
    def get_all_invited_accounts(cls, tel_number: str):
        tel_num = utl.check_number(tel_number)
        account = cls.get_account_or_404(phone_number=tel_num)
        return account.invited_accounts.all()


    @staticmethod
    def clean_all_accounts():
        Account.objects.all().delete()


    @classmethod
    def register_invite_code(cls, tel_number: str, invite_code: str):
        invited_account = cls.get_account_or_404(phone_number=tel_number)
        account_with_code = cls.get_account_or_404(invite_code=invite_code)
        invited_account.invite_account = account_with_code
        invited_account.save(); account_with_code.save()
        return invited_account

