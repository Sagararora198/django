from rest_framework import serializers
from .models import MenuItem



# class MenuItemSerializer(serializers.Serialize):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=5,decimal_places=2)
#     inventory = serializers.IntegerField()

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        
# for changing name and adding fields 
# from decimal import Decimal
# class MenuItemSerializer(serializers.ModelSerializer):
#     stock = serializers.IntegerField(source='inventory')
#     price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','stock','price_after_tax']
#     def calculate_tax(self,product:MenuItem):
#         return product.price * Decimal(1.1)    
