from django.urls import path
from .views import coordinate_list

# path urls for coordinateApi application.
urlpatterns = [
    path('coordinates/',coordinate_list),
]