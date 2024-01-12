from django.shortcuts import render

# Create your views here.
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import MenuItem
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        # items = MenuItem.objects.all()
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)  #lte less than equal to    
        if search:
            items = items.filter(title__contains=search)     #for case insensetive use icontains    
        serialized_items = MenuItemSerializer(items,many=True)   #the many=true signify you are converting list to json data
        return Response(serialized_items.data)
    if request.method == 'POST':
        serialized_items = MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data,status.HTTP_201_CREATED)
@api_view()
def single_item(request,id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem,pk=id)   #to get a json 404 error
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


        