from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .service import AccountService

from . import serializers as srl


class AccountList(APIView):
    def post(self, request, format=None):
        serializer = srl.AccountCreateS(data=request.data)
        if serializer.is_valid():
            account = AccountService.register(tel_number=serializer.validated_data['phone_number'])
            serializer = srl.AccountDisplayS(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
