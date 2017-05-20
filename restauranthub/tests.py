# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin

from .models import Restaurant, RestaurantType, Cuisine, Food, Events, Offers

# Create your tests here.
def create_restaurant(restaurant_name):
    return Restaurant.objects.create(restaurant_name=restaurant_name)

class RestaurantModelTests(TestCase):
    def test_restaurant_object_creation(self):
        """
        Restaurant objects created must return true for isinstance() and 
        __str__() must be equal to restaurant_name
        """
        r = create_restaurant("Test Restaurant")
        self.assertIs(isinstance(r, Restaurant), True)
        self.assertEqual(r.__str__(), r.restaurant_name)

class RestaurantTypeModelTests(TestCase):
    def test_restauranttype_object_creation(self):
        """
        Restauranttype objects created must return true for isinstance() and 
        __str__() must be equal to restaurant_type
        """
        r = create_restaurant("Test Restaurant")
        rt = r.restauranttype_set.create(restaurant_type="Test RestaurantType")
        self.assertIs(isinstance(rt, RestaurantType), True)
        self.assertEqual(rt.__str__(), rt.restaurant_type)

class CuisineModelTests(TestCase):
    def test_cuisine_object_creation(self):
        """
        Cuisine objects created must return true for isinstance() and 
        __str__() must be equal to cuisine_name
        """
        r = create_restaurant("Test Restaurant")
        c = r.cuisine_set.create(cuisine_name="Test Cuisine")
        self.assertIs(isinstance(c, Cuisine), True)
        self.assertEqual(c.__str__(), c.cuisine_name)

class FoodModelTests(TestCase):
    def test_food_object_creation(self):
        """
        Food objects created must return true for isinstance() and 
        __str__() must be equal to food_name
        """
        r = create_restaurant("Test Restaurant")
        f = r.food_set.create(food_name="Test Food")
        self.assertIs(isinstance(f, Food), True)
        self.assertEqual(f.__str__(), f.food_name)

class EventsModelTests(TestCase):
    def test_events_object_creation(self):
        """
        Events objects created must return true for isinstance() and 
        __str__() must be equal to event_name
        """
        r = create_restaurant("Test Restaurant")
        e = r.events_set.create(event_name="Test Event", event_date=timezone.now() + datetime.timedelta(days=7))
        self.assertIs(isinstance(e, Events), True)
        self.assertEqual(e.__str__(), e.event_name)

    def test_event_date_with_past_date(self):
        """
        is_valid() must return False for old event dates
        """
        r = create_restaurant("Test Restaurant")
        e = r.events_set.create(event_name="Test Event", event_date=timezone.now() + datetime.timedelta(days=-7))
        self.assertEqual(e.is_valid(), False)

    def test_event_date_with_future_date(self):
        """
        is_valid() must return True for future event dates
        """
        r = create_restaurant("Test Restaurant")
        e = r.events_set.create(event_name="Test Event", event_date=timezone.now() + datetime.timedelta(days=7))
        self.assertEqual(e.is_valid(), True)

    def test_event_date_with_current_date(self):
        """
        is_valid() must return True for current event dates
        """
        r = create_restaurant("Test Restaurant")
        e = r.events_set.create(event_name="Test Event", event_date=timezone.now() + datetime.timedelta(hours=1))
        self.assertEqual(e.is_valid(), True)

class OffersModelTests(TestCase):
    def test_offers_object_creation(self):
        """
        Offers objects created must return true for isinstance() and 
        __str__() must be equal to offer_name
        """
        r = create_restaurant("Test Restaurant")
        o = r.offers_set.create(offer_name="Test Offer", offer_valid_date=timezone.now() + datetime.timedelta(days=7))
        self.assertIs(isinstance(o, Offers), True)
        self.assertEqual(o.__str__(), o.offer_name)

    def test_offer_valid_date_with_past_date(self):
        """
        is_valid() must return False for old offer dates
        """
        r = create_restaurant("Test Restaurant")
        o = r.offers_set.create(offer_name="Test Offer", offer_valid_date=timezone.now() + datetime.timedelta(days=-7))
        self.assertEqual(o.is_valid(), False)

    def test_offer_valid_date_with_future_date(self):
        """
        is_valid() must return True for future offer dates
        """
        r = create_restaurant("Test Restaurant")
        o = r.offers_set.create(offer_name="Test Offer", offer_valid_date=timezone.now() + datetime.timedelta(days=7))
        self.assertEqual(o.is_valid(), True)

    def test_offer_valid_date_with_current_date(self):
        """
        is_valid() must return True for current offer dates
        """
        r = create_restaurant("Test Restaurant")
        o = r.offers_set.create(offer_name="Test Offer", offer_valid_date=timezone.now() + datetime.timedelta(hours=1))
        self.assertEqual(o.is_valid(), True)

class RestaurantResourceTests(ResourceTestCaseMixin, TestCase):
    fixtures = ['test_restaurant.json'] 

    def setUp(self):
        super(RestaurantResourceTests, self).setUp() 

        self.restaurant_1 = Restaurant.objects.get(restaurant_name='Nepal Dairy')

        self.detail_url = '/api/v1/restaurant/{0}/'.format(self.restaurant_1.pk)

    def test_get_list_json(self):
        response = self.api_client.get('/api/v1/restaurant/', format='json')
        self.assertValidJSONResponse(response)

        self.assertEqual(len(self.deserialize(response)['objects']), 2)

        # TODO: getting error in following assert : TypeError: unhashable type : 'dict'
        # self.assertEqual(self.deserialize(response)['objects'][0], {
        #     {
        #         'address': 'Mahaboudha',
        #         'city': 'Kathmandu',
        #         'id': str(self.restaurant_1.pk),
        #         'latitude': '111.000.111.000',
        #         'longitude': '111.000.111.000',
        #         'resource_uri': '/api/v1/restaurant/{0}/'.format(self.restaurant_1.pk),
        #         'restaurant_name': 'Nepal Dairy'
        #         }
        #     })

    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/restaurant/', format='xml'))

    def test_get_detail_list_json(self):
        response = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(response)
        self.assertKeys(self.deserialize(response),['phone_number','city','cuisine','food','opening_hours','longitude','events','website','offers','restaurant_name','address','latitude','restauranttype','id','resource_uri'])

    def test_get_detail_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get(self.detail_url, format='xml'))



