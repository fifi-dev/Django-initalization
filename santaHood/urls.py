from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('', views.index, name='index'),
  #path('products/', views.products, name='products'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('shop/', views.shop, name='shop'),

  path('add/', add_product, name='add'),


]