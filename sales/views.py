from rest_framework import viewsets
from sales.serializers import SaleSerializers
from sales.models import Sale


class SaleAPIView(viewsets.ModelViewSet):
    serializer_class = SaleSerializers
    queryset = Sale.objects.all()
