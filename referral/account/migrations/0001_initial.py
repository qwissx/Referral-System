# Generated by Django 5.2.4 on 2025-07-23 21:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+999999999'. Максимум 15 цифр.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Номер телефона')),
                ('invite_code', models.CharField(max_length=10, unique=True, verbose_name='Инвайт-код')),
                ('invite_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_accounts', to='account.account')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
