from django.urls import path
from . import views

app_name = 'product'

urlpatterns =[
    path("", views.index, name='index'),
    path("<int:product_id>/", views.product_detail, name='product_detail')
    
]