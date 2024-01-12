from django.urls import path

from . import views

urlpatterns = [
    path('menu-items/',views.menu_items),
    path('single-item/<int:id>',views.single_item)
]