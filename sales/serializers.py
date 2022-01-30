from rest_framework import serializers

from sales.models import Sale


class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'