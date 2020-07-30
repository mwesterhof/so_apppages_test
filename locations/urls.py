from django.urls import re_path, path

from .views import LocationDetailView, LocationListView

urlpatterns = [
    re_path(r"^locations/$", LocationListView.as_view(), name="location_list"),
    path("location/<int:pk>/",
         LocationDetailView.as_view(), name="location"),
]
