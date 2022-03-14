from rest_framework import serializers
from main.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = "__all__"

class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = "__all__"