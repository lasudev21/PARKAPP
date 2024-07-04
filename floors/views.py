from django.shortcuts import render
from floors.models import Floors, Rows


def floor(request):
    floors = Floors.objects.all()
    return render(request, 'floors/index.html', {
        'title': 'Pisos',
        'data': floors
    })

def row(request):
    rows = Rows.objects.all()
    return render(request, 'rows/index.html', {
        'title': 'Filas',
        'data': rows
    })


def parkinglot(request):
    floors = Floors.objects.all()
    rows = Rows.objects.all()

    return render(request, 'parkinglots/index.html', {
        'title': 'Estacionamientos',
        'floors': floors
    })