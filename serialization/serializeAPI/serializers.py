from rest_framework import serializers
from .models import MenuItem
from .models import Category
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=5,decimal_places=2)
#     inventory = serializers.IntegerField()
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']    
    
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    # category = serializers.StringRelatedField()
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock','category']  