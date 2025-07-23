from django.db import models
from django.contrib.auth.models import User

from . import utils as utl


class Account(models.Model):
    invite_account = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        related_name='invited_accounts',
    )
    phone_number = models.CharField(
        validators=[utl.phone_regex],
        max_length=17,
        unique=True,
        verbose_name='Номер телефона'
    )
    invite_code = models.CharField(
        max_length=10,
        unique=True,
        null=False,
        verbose_name='Инвайт-код'
    )

    def __str__(self):
        return f'{self.phone_number} - {self.invite_code}'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
