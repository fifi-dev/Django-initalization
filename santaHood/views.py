from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
  return render(request, 'santaHood/index.html')

from .forms import ProductForm

def add_product(request):
    context ={}

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "santaHood/add_product.html", context)

def cart(request):
  context ={}
  return render(request, 'santaHood/cart.html', context)

def checkout(request):
  context ={}
  return render(request, 'santaHood/checkout.html', context)

def shop(request):
  context ={}
  return render(request, 'santaHood/shop.html', context)