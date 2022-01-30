from rest_framework import viewsets
from address.serializers import AddresSerializers
from address.models import Addres


from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class AddresAPIView(viewsets.ModelViewSet):
    serializer_class = AddresSerializers
    queryset = Addres.objects.all()
   

    @action(detail=False, methods=['get'])
    def street(self, request, pk=None):
        search = request.query_params.get('search')
        queryset = self.get_queryset().filter(street__icontains=search)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


