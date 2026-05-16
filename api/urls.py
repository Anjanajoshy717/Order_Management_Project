"""
URL configuration for order_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ProductListCreateView, ProductDetailView, CreateOrderView, OrderListView, OrderUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('products/',ProductListCreateView.as_view(),name='products'),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('orders/create/',CreateOrderView.as_view(),name='create-order'),
    path('orders/',OrderListView.as_view(),name='orders'),
    path('orders/<int:pk>/',OrderUpdateView.as_view(),name='order-update'),
]

