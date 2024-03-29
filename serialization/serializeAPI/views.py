from django.shortcuts import render

# Create your views here.
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import MenuItem
from django.core.paginator import Paginator,EmptyPage
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        # items = MenuItem.objects.all()
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        odering = request.query_params.get('odering')
        perpage = request.query_params.get('perpage',default=2)
        page = request.query_params.get('page',default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)  #lte less than equal to    
        if search:
            items = items.filter(title__contains=search)     #for case insensetive use icontains    
        if odering:
            odering_fields =    odering.split(",")
            
            items = items.order_by(*odering_fields)  # odering will be done  in ascending order for descending order just add - in api call no need to add any code  
        paginator = Paginator(items,per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []           #if page number does not exist then it will generate emptypage error and items will be empty
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



from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"This is a protected route"})        


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exist():
        return Response({"message":"Only by Manager"})
    else:
        return Response({"message":"only manager can access"},403)