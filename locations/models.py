from django.db import models

from wagtail.core.models import Page
from wagtail_app_pages.models import AppPageMixin


STATES = [
    ('a', 'A'),
    ('b', 'B'),
]


class Feature(models.Model):
    feature = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ['feature']
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.feature


class Location(models.Model):

    template = 'locations/locations_list.html'

    name = models.CharField(max_length=30, null=True, blank=False)
    address = models.CharField(max_length=60, null=True, blank=False)
    city = models.CharField(max_length=25)
    state = models.CharField(
        max_length=2, choices=STATES, null=True, blank=False)
    zipcode = models.CharField(max_length=5, null=True, blank=False)
    lat = models.CharField(max_length=50, null=True, blank=False)
    lon = models.CharField(max_length=50, null=True, blank=False)
    phone = models.CharField(max_length=10, null=True, blank=False)
    email = models.CharField(max_length=40, null=True, blank=False)
    places_id = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    google_url = models.CharField(max_length=100, null=True, blank=True)
    entity = models.CharField(max_length=10, null=True, blank=True)
    truck_url = models.CharField(max_length=100, null=True, blank=True)
    trailer_url = models.CharField(max_length=100, null=True, blank=True)
    supplies_url = models.CharField(max_length=100, null=True, blank=True)
    features = models.ManyToManyField(Feature)

    class Meta:  # noqa
        ordering = ['name']
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class LocationPage(AppPageMixin, Page):
    template = 'locations/locations_page.html'
    url_config = 'locations.urls'

    class Meta:  # noqa
        verbose_name = "Locations List"
        verbose_name_plural = "Locations Lists"
