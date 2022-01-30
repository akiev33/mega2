from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


from rest_framework import viewsets
from product.serializers import ProductSerializers
from product.models import Product


class ProductAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.order_by('-price_for_one')


    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        s = request.query_params.get('s')
        queryset = self.get_queryset().filter(name__icontains=t)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def price(self, request, pk=None):
        max_price = request.query_params.get('max_price')
        queryset = self.queryset.filter(price_for_one__lte=max_price)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)