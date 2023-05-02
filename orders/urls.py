from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.CartSummaryView.as_view(), name='cart_summary'),
    path('', views.cart_add, name='cart_add'),
    path('', views.CartDeleteView.as_view(), name='cart_delete'),
    path('', views.CartUpdateView.as_view(), name='cart_update'),

]
