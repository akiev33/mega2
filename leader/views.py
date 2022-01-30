from rest_framework import viewsets
from leader.serializers import LeaderSerializers
from leader.models import Leader


class LeaderAPIView(viewsets.ModelViewSet):
    serializer_class = LeaderSerializers
    queryset = Leader.objects.all()
    

