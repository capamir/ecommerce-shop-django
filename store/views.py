from django.shortcuts import render, get_list_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product, Category

# Create your views here.
class StoreView(ListView):
    template_name = "store/store.html"
    model = Product 
    context_object_name = "products"

class ProductDetailsView(DetailView):
    template_name = "store/product_details.html"
    model = Product
    context_object_name = "product"

# class ListCategotyView(View):
#     template_name = "store/list_categoty.html"

#     def get(self, request, slug=None):
#         category = get_list_or_404(Category, slug=slug)
#         products = Product.objects.filter(category=category)
        
#         context = {
#             'category': category,
#             'products': products,
#         }
#         return render(request, self.template_name, context)
    
class ListCategotyView(DetailView):
    template_name = "store/list_category.html"
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=context['category'])
        return context
    