from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class CartSummaryView(TemplateView):
    template_name = 'orders/cart_summary.html'

class CartAddView(View):
    pass

class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
