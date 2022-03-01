from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('', index, name='index'),
  #path('products/', views.products, name='products'),
  path('cart/', cart, name='cart'),
  path('shop/', shop, name='shop'),

  path('add/', add_product, name='add'),
  path('shop/<slug>', detail_view, name='detail_view' ),
]