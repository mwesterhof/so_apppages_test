from django.urls import re_path

from .views import LocationDetailView, LocationListView

urlpatterns = [
    re_path(r"^locations/?$", LocationListView.as_view(), name="location_list"),
    re_path(r"^location/<int:pk>/?$",
         LocationDetailView.as_view(), name="location"),
]
