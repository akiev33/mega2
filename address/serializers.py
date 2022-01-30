from rest_framework import serializers
from address.models import Addres


class AddresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = '__all__'