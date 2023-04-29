from django.shortcuts import render
from django.views import View

# Create your views here.
class CartSummaryView(View):
    template_name = 'orders/cart_summary.html'

class CartAddView(View):
    pass

class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
