from django.urls import path

from .views import floor, parkinglot, saveSimulation, getSimulation

urlpatterns = [
    path('floors/', floor, name='floors'),
    path('parkinglots/', parkinglot, name='parkinglots'),
    path('simulation/', getSimulation, name="simulation"),
    path('savesimulation/', saveSimulation, name='savesimulation'),
]