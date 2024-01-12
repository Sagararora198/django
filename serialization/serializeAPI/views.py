from django.shortcuts import render

# Create your views here.
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MenuItem
@api_view()
def menu_items(request):
    # items = MenuItem.objects.all()
    items = MenuItem.objects.select_related('category').all()
    serialized_items = MenuItemSerializer(items,many=True)   #the many=true signify you are converting list to json data
    return Response(serialized_items.data)
    
@api_view()
def single_item(request,id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem,pk=id)   #to get a json 404 error
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


        