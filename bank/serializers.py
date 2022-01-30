from rest_framework import serializers
from bank.models import Bank_account


class Bank_accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank_account
        fields = '__all__'