from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
        model = Product
        fields = "__all__"

class QuantityForm(forms.Form):
  quantity = forms.IntegerField()