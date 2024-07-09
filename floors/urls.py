from django.urls import path

from .views import floor, deleteFloor, parkinglot, saveSimulation, getSimulation, parking

urlpatterns = [
    path('floors/', floor, name='floors'),
    path('floors_delete/', deleteFloor, name='floors_delete'),
    path('parkinglots/', parkinglot, name='parkinglots'),
    path('simulation/', getSimulation, name="simulation"),
    path('savesimulation/', saveSimulation, name='savesimulation'),
    path('parkings/', parking, name='parkings'),
]