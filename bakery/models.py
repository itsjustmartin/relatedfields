from django.db import models


class Food(models.Model):
    name = models.TextField(unique=True)
    price = models.PositiveIntegerField()

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name


class Address(models.Model):
    street_name = models.TextField()
    city = models.TextField()


class Customer(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    food = models.ManyToManyField(Food, related_name="orders")
