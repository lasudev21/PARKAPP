from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from floors.models import Floors, ParkingLots, Spaces
import json

def floor(request):
    floors = Floors.objects.all()
    return render(request, 'floors/index.html', {
        'title': 'Pisos',
        'breadcrumb': ['Maestras', 'Pisos'],
        'data': floors
    })

def parkinglot(request):
    floors = Floors.objects.all()
    parkinglots = ParkingLots.objects.all()

    return render(request, 'parkinglots/index.html', {
        'title': 'Estacionamientos',
        'breadcrumb': ['Maestras', 'Estacionamientos'],
        'floors': floors,
        'parkinglots': parkinglots,
    })

def saveSimulation(request):
    if request.method == 'POST':
        try:
            floor = Floors.objects.get(id = request.POST.get('floor', ''))
            parkinglot = ParkingLots.objects.filter(floor = request.POST.get('floor', ''))
            if request.POST.get('orientation', '') == "HORIZONTAL":
                orientation = "H"
            else:
                orientation = "V"
            
            data = json.loads(request.POST.get('spaces'))
            print(data)

            if(parkinglot.exists()):
                parkinglot.update(
                    name = request.POST.get('name', ''),
                    orientation = orientation,
                    numberparq = request.POST.get('numberparq', ''),
                    numberrows = request.POST.get('numberrows', '') ,
                )
                # print(spaces)
                for obj in data:
                    space = Spaces.objects.filter(name = obj.get('name'))
                    if(space.exists()):
                        space.update(
                            name = obj.get('name'),
                            status = obj.get('status')
                        )
                    else:
                         Spaces.objects.create(
                            parkinglot = parkinglot[0],
                            name = obj.get('name'),
                            status = obj.get('status')
                        )
            else:
                new_parkinglot = ParkingLots(
                    name = request.POST.get('name', ''),
                    floor = floor,
                    orientation = orientation,
                    numberparq = request.POST.get('numberparq', ''),
                    numberrows = request.POST.get('numberrows', '') ,               
                )
                new_parkinglot.save()

                for obj in data:
                    Spaces.objects.create(
                        parkinglot = new_parkinglot,
                        name = obj.get('name'),
                        status = obj.get('status')
                    )

            return JsonResponse({'success' : True, 'message': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'success' : False, 'message': str(e)})

def getSimulation(request):
    if request.method == 'POST':
        parkinglot = ParkingLots.objects.filter(floor = request.POST.get('floor', ''))
        if(parkinglot.exists()):
            parkinglotObj = {
                'id': parkinglot[0].id,
                'numberrows': parkinglot[0].numberrows, 
                'numberparq' : parkinglot[0].numberparq,
                'orientation' : parkinglot[0].orientation,
            }
            # print(parkinglot[0])
            spaces = Spaces.objects.filter(parkinglot = parkinglot[0])
            print(spaces)
            spacesObj = []
            for obj in spaces:
                spacesObj.append({'name': obj.name, 'status' : obj.status})

            return JsonResponse({'success' : True, 'parkinglot': parkinglotObj, 'spaces' : spacesObj})
        else:
            return JsonResponse({'success' : False, 'parkinglot': {}, 'spaces' : []})

