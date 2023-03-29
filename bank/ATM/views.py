from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Accounts, Transactions
from django.core import serializers
from .serializers import AccountsSerializer, TransactionsSerializer

# Create your views here.
class ViewAccount(APIView):
    def get(self, request):
        requested_id = request.data.get("id")
        try:
            account = Accounts.objects.get(id=requested_id)
            serializer = AccountsSerializer(account)
            return Response(serializer.data, status.HTTP_200_OK)
        except Accounts.DoesNotExist:
            return Response("Account not found", status.HTTP_404_NOT_FOUND)
        
class ViewAccountFromURL(APIView):
    def get(self, request, id):
        requested_id = id
        try:
            account = Accounts.objects.get(id=requested_id)
            serializer = AccountsSerializer(account)
            return Response(serializer.data, status.HTTP_200_OK)
        except Accounts.DoesNotExist:
            return Response("Account not found", status.HTTP_404_NOT_FOUND)

class ViewTransaction(APIView):
    def get(self, request):
        requested_id = request.data.get("id")
        try:
            transaction = Transactions.objects.get(id=requested_id)
            serializer = TransactionsSerializer(transaction)
            return Response(serializer.data, status.HTTP_200_OK)
        except Transactions.DoesNotExist:
            return Response("Transaction does not exist", status.HTTP_404_NOT_FOUND)

        
class ViewTransactionFromURL(APIView):
    def get(self, request, id):
        requested_id = id
        try:
            transaction = Transactions.objects.get(id=requested_id)
            serializer = TransactionsSerializer(transaction)
            return Response(serializer.data, status.HTTP_200_OK)
        except Transactions.DoesNotExist:
            return Response("Transaction does not exist", status.HTTP_404_NOT_FOUND)
        
class NewTransaction(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TransactionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class CreateAccount(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AccountsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)