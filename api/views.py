from django.shortcuts import render
from rest_framework import generics, status
from api.serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import Product
from api.permissions import IsAdminUserRole
from api.serializers import ProductSerializer
from rest_framework.response import Response
from api.permissions import IsCustomerUserRole
from api.serializers import CreateOrderSerializer, OrderSerializer
from api.models import Order

#register view
class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

#product create+list
class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_permissions(self):
        if self.request.method=='POST':
            return [IsAuthenticated(), IsAdminUserRole()]
        return [IsAuthenticated()]

#product update delete
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated,IsAdminUserRole]

#create order
class CreateOrderView(generics.CreateAPIView):
    serializer_class=CreateOrderSerializer
    permission_classes=[IsAuthenticated, IsCustomerUserRole]
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        order=serializer.save()
        response_serializer=OrderSerializer(order)
        return Response(response_serializer.data,status=status.HTTP_201_CREATED)

#list orders
class OrderListView(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        if user.role=='admin':
            return Order.objects.all()
        return Order.objects.filter(customer=user)

#update order status
class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated, IsAdminUserRole]

