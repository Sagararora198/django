from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/',views.menu_items),
    path('single-item/<int:id>',views.single_item),
    path('secret/',views.secret),
    path('api-token-auth',obtain_auth_token) ,   #this endpoint only accept post request (add username and password) hit the endpoint for tokens
    path('manager/',views.manager_view),
]