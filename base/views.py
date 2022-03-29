from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FoydalanuvchiSerializer, ProductSerializer, StatSerializer
from .models import MainUser, Product, Stats
from rest_framework.decorators import action
from rest_framework.response import Response

class FoydalanuvchiViewSet(ModelViewSet):
    queryset = MainUser.objects.all()
    serializer_class = FoydalanuvchiSerializer

    @action(detail=True, methods=["GET"])
    def products(self, request, pk,  *args, **kwargs):
        user = MainUser.objects.get(id=pk)
        products = Product.objects.filter(user=user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StatsViewSet(ModelViewSet):
    queryset = Stats.objects.all()
    serializer_class = StatSerializer

