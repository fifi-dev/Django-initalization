from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
  return render(request, 'santaHood/index.html')

def cart(request):
  context ={}
  return render(request, 'santaHood/cart.html', context)

def checkout(request):
  context ={}
  return render(request, 'santaHood/checkout.html', context)

def shop(request):
  context ={}
  return render(request, 'santaHood/shop.html', context)