from django.urls import path

from .views import floor, parkinglot, saveSimulation

urlpatterns = [
    path('floors/', floor, name='floors'),
    path('parkinglots/', parkinglot, name='parkinglots'),
    path('savesimulation/', saveSimulation, name='savesimulation'),
]