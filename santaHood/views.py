from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Product

# Create your views here.
def index(request):
  return render(request, 'santaHood/index.html')

from .forms import *

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

def detail_view(request, slug):
    
    context ={}

    context["data"] = Product.objects.get(slug = slug)
    
    return render(request, "santaHood/product_detail.html", context)

def shop(request):
  context ={}
  context["dataset"] = Product.objects.all()
  return render(request, 'santaHood/shop.html', context)

def update_quantity(request,slug):
    context = {}

    obj = get_object_or_404(Product, slug = slug)

    form = QuantityForm(request.POST)
    if form.is_valid():
        obj.quantity-=form.cleaned_data['quantity']
        if obj.quantity < 0:
          return HttpResponseRedirect("/shop/"+slug)
        obj.save()
        return HttpResponseRedirect("/shop/"+slug)

    context["form"] = form

    return render(request, "santaHood/product_update.html", context)