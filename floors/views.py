from django.shortcuts import render
from django.http import JsonResponse
from floors.models import Floors, ParkingLots


def floor(request):
    floors = Floors.objects.all()
    return render(request, 'floors/index.html', {
        'title': 'Pisos',
        'data': floors
    })

def parkinglot(request):
    floors = Floors.objects.all()
    parkinglots = ParkingLots.objects.all()

    return render(request, 'parkinglots/index.html', {
        'title': 'Estacionamientos',
        'floors': floors,
        'parkinglots': parkinglots,
    })

def saveSimulation(request):
    if request.method == 'POST':
        try:
            # parkinglot = ParkingLots.objects.filter(floor = request.POST.get('floor', ''))
            # if(parkinglot.exists()):
            #     return JsonResponse({'success' : False, 'message': 'Ya existe un modelo de estacionamiento para el piso seleccionado'})

            # floor = Floors.objects.get(id = request.POST.get('floor', ''))
            # if request.POST.get('orientation', '') == "HORIZONTAL":
            #     orientation = "H"
            # else:
            #     orientation = "V"

            # ParkingLots.objects.create(
            #     name = request.POST.get('name', ''),
            #     floor = floor,
            #     orientation = orientation,
            #     numberparq = request.POST.get('numberparq', ''),
            #     numberrows = request.POST.get('numberrows', '') ,               
            # )
            return JsonResponse({'success' : True, 'message': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'success' : False, 'message': str(e)})