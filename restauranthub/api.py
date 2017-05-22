from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields

from restauranthub.models import Restaurant, RestaurantType, Cuisine, Food, Events, Offers

class RestaurantTypeResource(ModelResource):
    restaurant = fields.ManyToManyField('restauranthub.api.RestaurantResource', 'restaurant', related_name='restauranttype_set')
    class Meta:
        queryset = RestaurantType.objects.all()
        resource_name = 'restauranttype'


class CuisineResource(ModelResource):
    restaurant = fields.ManyToManyField('restauranthub.api.RestaurantResource', 'restaurant', related_name='cuisine_set')
    class Meta:
        queryset = Cuisine.objects.all()
        resource_name = 'cuisine'


class FoodResource(ModelResource):
    restaurant = fields.ManyToManyField('restauranthub.api.RestaurantResource', 'restaurant', related_name='food_set')
    class Meta:
        queryset = Food.objects.all()
        resource_name = 'food'


class RestaurantResource(ModelResource):
    restauranttype = fields.ManyToManyField(RestaurantTypeResource, 'restauranttype_set', full=True, full_detail=True)
    cuisine = fields.ManyToManyField(CuisineResource, 'cuisine_set', full=True, full_detail=True)
    food = fields.ManyToManyField(FoodResource, 'food_set', full=True, full_detail=True)
    events = fields.ManyToManyField('restauranthub.api.EventsResource', 'events_set', related_name='restaurant')
    offers = fields.ManyToManyField('restauranthub.api.OffersResource', 'offers_set', related_name='restaurant')
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'
        filtering = {'restaurant_name': ALL}
        # authentication = BasicAuthentication()
        authentication = ApiKeyAuthentication()

class EventsResource(ModelResource):
    restaurant = fields.ForeignKey(RestaurantResource, 'restaurant')
    class Meta:
        queryset = Events.objects.all()
        resource_name = 'events'

class OffersResource(ModelResource):
    restaurant = fields.ForeignKey(RestaurantResource, 'restaurant')
    class Meta:
        queryset = Offers.objects.all()
        resource_name = 'offers'

