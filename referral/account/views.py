from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .service import AccountService

from . import serializers as srl


class AccountList(APIView):
    def delete(self, request, format=None):
        AccountService.clean_all_accounts()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)


class AccountDetails(APIView):
    def get(self, request, pk, format=None):
        account = AccountService.get_account_or_404(phone_number=pk)
        serializer = srl.AccountDisplayS(account)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = srl.AccountInviteCodeS(data=request.data)
        if serializer.is_valid():
            account = AccountService.register_invite_code(
                tel_number=pk,
                invite_code=serializer.validated_data['invite_code'],
            )
            serializer = srl.AccountDisplayS(account)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailsList(APIView):
    def get(self, request, pk, format=None):
        accounts = AccountService.get_all_invited_accounts(tel_number=pk)
        serializer = srl.AccountDisplayS(accounts, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def start_register(request):
    serializer = srl.AccountCreateSS(data=request.data)
    if serializer.is_valid():
        message = AccountService.start_register(tel_number=serializer.validated_data['phone_number'])
        return Response({'message': message}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def end_register(request):
    serializer = srl.AccountCreateES(data=request.data)
    if serializer.is_valid():
        account = AccountService.end_register(verification_code=serializer.validated_data['verification_code'])
        serializer = srl.AccountDisplayS(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

