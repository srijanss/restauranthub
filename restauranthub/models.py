# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Restaurant(models.Model):
    """
    Restaurant Model that holds Retaurant Details like Name, Address, Contact details
    """
    restaurant_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.restaurant_name

@python_2_unicode_compatible
class RestaurantType(models.Model):
    """
    RestaruantType Model holds the type of restaurant like, Dining, Cafe, Desserts
    """
    restaurant = models.ManyToManyField(Restaurant)
    restaurant_type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.restaurant_type

@python_2_unicode_compatible
class Cuisine(models.Model):
    """
    Cuisine Model holds the name of different cuisines that restaurant have like Italian, Chinese, Indian
    """
    restaurant = models.ManyToManyField(Restaurant)
    cuisine_name  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.cuisine_name

@python_2_unicode_compatible
class Food(models.Model):
    """
    Food Model holds list of different foods like Pizza, MoMo, Thakali set
    """
    restaurant = models.ManyToManyField(Restaurant)
    food_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.food_name

@python_2_unicode_compatible
class Events(models.Model):
    """
    Events organised by Restaurant on specific date
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField("event date")

    def __str__(self):
        return self.event_name

    def is_valid(self):
        return self.event_date > timezone.now()

@python_2_unicode_compatible
class Offers(models.Model):
    """
    Offers and Deals provided by the Restaurant 
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    offer_name = models.CharField(max_length=100)
    offer_details = models.CharField(max_length=200)
    offer_valid_date = models.DateField("offer valid upto date")

    def __str__(self):
        return self.offer_name

    def is_valid(self):
        return self.offer_valid_date > timezone.now()

@python_2_unicode_compatible
class RestaurantOwner(models.Model):
    """
    Restaurant Owner user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.username

@python_2_unicode_compatible
class Customer(models.Model):
    """
    Customer or Diner that is user that books table 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateField("joining date")
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return "Customer Joined the Hub on " + str(self.date_joined)

