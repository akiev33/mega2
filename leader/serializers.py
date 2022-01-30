from rest_framework import serializers
from leader.models import Leader


class LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'


class First_nameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['first_name', 'company']




