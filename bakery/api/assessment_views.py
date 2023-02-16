# This file does not need to be changed

from rest_framework import views, generics
from rest_framework.response import Response

from bakery.api.assessment_data import test_data
from bakery.api.assessment_serializers import (
    NameAndCountSerializer,
    AddressSerializer,
    FoodSerializer,
)
from bakery.api.serializers import CustomerSerializer, OrderSerializer
from bakery.models import Address, Food, Customer, Order


class Question1View(views.APIView):
    def get(self, request):
        return Response({"username": request.user.username})


class NameAndCountBaseView(views.APIView):
    def get(self, request, pk=None):
        if not pk:
            return Response(NameAndCountSerializer(test_data, many=True).data)

        return Response(NameAndCountSerializer(test_data[int(pk) - 1]).data)

    def post(self, request):
        serializer = NameAndCountSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        return Response(serializer.data)

    def put(self, request, pk):
        serializer = NameAndCountSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        return Response(serializer.data)

    def delete(self, request, pk):
        return Response(status=204)


class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class FoodListView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
