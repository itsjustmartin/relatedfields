from rest_framework import serializers

# Question 3, 4, 5: Add any imports you need
from bakery.models import Food, Customer, Order


class OrderSerializer(serializers.ModelSerializer):
    # Question 3: Add your fields here
    food = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Food.objects.all()
    )

    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # Question 4: Add your fields here

    class Meta:
        model = Customer
        fields = "__all__"

    # Question 5: Implement your methods here
