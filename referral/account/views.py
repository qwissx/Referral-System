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
        return render(request, 'profile.html', {'account': account})

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


@api_view(['POST'])
def send_code(request):
    serializer = srl.AccountCreateSS(data=request.data)
    if serializer.is_valid():
        message = AccountService.send_code(tel_number=serializer.validated_data['phone_number'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_code(request):
    serializer = srl.AccountCreateES(data=request.data)
    if serializer.is_valid():
        account = AccountService.verify_code(verification_code=serializer.validated_data['verification_code'])
        serializer = srl.AccountDisplayS(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def send_code_form(request):
    return render(request, 'send_code.html')

@api_view(['GET'])
def verify_code_form(request):
    return render(request, 'verify_code.html')
