from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.CartSummaryView.as_view(), name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/<str:pk>/', views.CartDeleteView.as_view(), name='cart_delete'),
    path('update/<str:pk>/', views.CartUpdateView.as_view(), name='cart_update'),

]
