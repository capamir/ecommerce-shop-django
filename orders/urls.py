from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartSummaryView.as_view(), name='cart_summary'),
    path('', views.CartAddView.as_view(), name='cart_add'),
    path('', views.CartDeleteView.as_view(), name='cart_delete'),
    path('', views.CartUpdateView.as_view(), name='cart_update'),

]
