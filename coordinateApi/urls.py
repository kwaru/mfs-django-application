from django.urls import path
from .views import coordinate_list

urlpatterns = [
    path('coordinates/',coordinate_list),
]