from rest_framework import viewsets
from bank.serializers import Bank_accountSerializers
from bank.models import Bank_account


class Bank_accountAPIView(viewsets.ModelViewSet):
    serializer_class = Bank_accountSerializers
    queryset = Bank_account.objects.all()
    