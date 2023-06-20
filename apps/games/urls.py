from django.urls import path
from .views import index, random, about, roundd

urlpatterns = [
    path('main/', index),
    path('random/', random),
    path('about/', about),
    path('round/', roundd)
]