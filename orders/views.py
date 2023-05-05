from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from .cart import Cart
from store.models import Product

# Create your views here.
class CartSummaryView(TemplateView):
    template_name = 'orders/cart_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class CartAddView(View):
    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)

    def post(self, request):
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty')) 
        product = get_object_or_404(Product, pk=product_id)
        self.cart.add(product, product_qty)

        response = JsonResponse({
            'qty': self.cart.__len__()
        })
        return response
    
        
class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
