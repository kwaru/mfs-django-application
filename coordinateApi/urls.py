from django.urls import path
from .views import ListVIewpAPI, DetailedViewAPI

# path urls for coordinateApi application.
urlpatterns = [
    path('api/v1/coordinates/',ListVIewpAPI.as_view()),
    path('api/v1/coordinates/<int:pk>/',DetailedViewAPI.as_view()),
]