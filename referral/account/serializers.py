from rest_framework import serializers

from .models import Account

class AccountCreateS(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=30)

class AccountInviteCodeS(serializers.Serializer):
    invite_code = serializers.CharField(required=True, max_length=6, min_length=6)

class AccountDisplayS(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

