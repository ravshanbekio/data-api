from rest_framework.serializers import ModelSerializer
from .models import MainUser, Product, Stats

class FoydalanuvchiSerializer(ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StatSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'