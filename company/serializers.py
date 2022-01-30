from rest_framework import serializers
from company.models import Company


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class Name_companySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']
