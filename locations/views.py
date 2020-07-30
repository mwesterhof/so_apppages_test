from django.views.generic import DetailView, ListView
from .models import Location


def getGoogleReviews(foo):
    return


def getWSSUnits(foo):
    return


class LocationDetailView(DetailView):

    model = Location

    context_object_name = "location"
    queryset = Location.objects.all()
    template_name = "locations/location_details.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        places_id = self.object.places_id
        entity = self.object.entity

        reviews = getGoogleReviews(places_id)
        units = getWSSUnits(entity)
        context = self.get_context_data(
            object=self.object, reviews=reviews, units=units)

        return self.render_to_response(context)


class LocationListView(ListView):

    model = Location
