from rest_framework import serializers

from .models import Account

class AccountCreateSS(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=30)

class AccountCreateES(serializers.Serializer):
    verification_code = serializers.CharField(required=True, max_length=4)

class AccountInviteCodeS(serializers.Serializer):
    invite_code = serializers.CharField(required=True, max_length=6, min_length=6)

class AccountDisplayS(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "phone_number", "invite_account", "invite_code"]
