# This file does not need to be changed

from rest_framework import serializers

from bakery.api.assessment_data import NameAndCount
from bakery.models import Address, Food


class NameAndCountSerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.count = validated_data["count"]
        return instance

    def create(self, validated_data):
        return NameAndCount(**validated_data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
