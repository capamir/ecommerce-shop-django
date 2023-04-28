from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product

# Create your views here.
class StoreView(ListView):
    template_name = "store/store.html"
    model = Product 
    context_object_name = "products"

class ProductDetailsView(DetailView):
    template_name = "store/product_details.html"
    model = Product
    context_object_name = "product"
