from rest_framework import viewsets
from estate.models import Estate, Unit, EstateType
from estate.serializers import EstateSerializer, UnitSerializer, EstateTypeSerializer


# Create your views here.
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer


class EstateTypesViewSet(viewsets.ModelViewSet):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer
