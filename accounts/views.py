from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from accounts.models import Account
from accounts.serializers import AccountSerializer
from accounts.permissions import isAdminOrOwner


class ListCreateAccountsView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ListAccountsByNewestView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        num = self.kwargs["num"]
        return self.queryset.order_by('-date_joined')[0:num]


class UpdateAccountView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
