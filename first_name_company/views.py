from rest_framework import viewsets
from leader.serializers import First_nameSerializers
from leader.models import Leader


class First_nameAPIView(viewsets.ModelViewSet):
    serializer_class = First_nameSerializers
    queryset = Leader.objects.all()