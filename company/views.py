from rest_framework import viewsets
from company.serializers import CompanySerializers
from company.models import Company


from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q


class CompanyAPIView(viewsets.ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.order_by('name')


    @action(detail=False, methods=['get'])
    def alphabet(self, request, pk=None):
        fromm = request.query_params.get('fromm')
        to = request.query_params.get('to')
        queryset = self.queryset.filter(
            Q(name__gte=fromm) &
            Q(name__lte=to)
        )
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
