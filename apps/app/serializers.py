from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance=instance.category).data
        return representation


class ProTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProType
        fields = ['type','name','size','price','discount']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type'] = ProductSerializer(instance=instance.type).data
        return representation
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
class ImageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageService
        fields = '__all__'

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = '__all__'
        
        
        

# Orders



# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
        
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'