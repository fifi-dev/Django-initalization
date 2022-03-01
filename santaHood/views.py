from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
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

def detail_view(request, slug):
    
    context ={}

    context["data"] = Product.objects.get(slug = slug)
    
    return render(request, "santaHood/product_detail.html", context)

def shop(request):
  context ={}
  context["dataset"] = Product.objects.all()
  return render(request, 'santaHood/shop.html', context)