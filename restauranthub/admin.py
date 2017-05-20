# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Restaurant, RestaurantType, Cuisine, Food, Events, Offers

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(RestaurantType)
admin.site.register(Cuisine)
admin.site.register(Food)
admin.site.register(Events)
admin.site.register(Offers)

