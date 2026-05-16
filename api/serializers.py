from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from api.models import User
from api.models import Product
from api.models import OrderItem
from api.models import Order

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password','role']

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user=User.objects.create_user(username=validated_data['username'],email=validated_data['email'],
                                        password=validated_data['password'],role='customer')
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name',read_only=True)
    subtotal=serializers.SerializerMethodField()
    class Meta:
        model=OrderItem
        fields=['id','product','product_name','quantity','price','subtotal']

    def get_subtotal(self, obj):
        return obj.price * obj.quantity

class CreateOrderItemSerializer(serializers.Serializer):
    product=serializers.IntegerField()
    quantity=serializers.IntegerField()

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True, read_only=True)
    total_amount=serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id','customer','status','created_at','items','total_amount']

    def get_total_amount(self, obj):
        return obj.total_amount()

class CreateOrderSerializer(serializers.Serializer):
    items=CreateOrderItemSerializer(many=True)
    def create(self, validated_data):
        user=self.context['request'].user
        items_data=validated_data['items']
        order=Order.objects.create(customer=user)
        for item_data in items_data:
            product_id=item_data['product']
            quantity=item_data['quantity']
            product=Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order,product=product,quantity=quantity,price=product.price)
        return order