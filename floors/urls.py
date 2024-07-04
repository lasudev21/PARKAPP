from django.urls import path

from .views import floor, row, parkinglot

urlpatterns = [
    path('floors/', floor, name='floors'),
    path('rows/', row, name='rows'),
    path('parkinglots/', parkinglot, name='parkinglots'),
]