from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('category/<slug:slug>/', views.StoreView.as_view(), name='category-filter'),
    path('product/<slug:slug>/', views.ListCategotyView.as_view(), name='product-details'),
]
