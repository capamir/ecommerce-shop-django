from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .cart import Cart
from store.models import Product

# Create your views here.
class CartSummaryView(TemplateView):
    template_name = 'orders/cart_summary.html'

class CartAddView(View):
    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty')) 
        product = get_object_or_404(Product, pk=product_id)
        self.cart.add(product, product_qty)

        
class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
