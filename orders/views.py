from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from .cart import Cart
from store.models import Product

# Create your views here.
class CartSummaryView(TemplateView):
    template_name = 'orders/cart_summary.html'


def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty')) 
        product = get_object_or_404(Product, pk=product_id)
        cart.add(product, product_qty)

        response = JsonResponse({
            'qty': product_qty
        })
        return response
        
    
        
class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
