from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from floors.models import Floors, ParkingLots, Spaces, History
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
import json

def floor(request):
    if request.method == 'POST':
        floorDato = Floors.objects.filter(id = request.POST.get('id', ''))
        name = request.POST.get('name', '').upper()
        if(floorDato.exists()):
            floorDato.update(
                name = name,
            )
        else:
            Floors.objects.create(
                name = name,
            )

        return JsonResponse({'success' : True, 'message': 'Datos guardados correctamente'})

    floors = Floors.objects.order_by('-created_at').all()
    return render(request, 'floors/index.html', {
        'title': 'Pisos',
        'breadcrumb': ['Maestras', 'Pisos'],
        'data': floors
    })

def deleteFloor(request):
    if request.method == 'POST':
        floorDel = get_object_or_404(Floors, id = request.POST.get('id', ''))
        floorDel.delete()

        return JsonResponse({'success' : True, 'message': 'Dato eliminado correctamente'})
    
def parkinglot(request):
    floors = Floors.objects.order_by('name').all()
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

            if(parkinglot.exists()):
                parkinglot.update(
                    name = request.POST.get('name', ''),
                    orientation = orientation,
                    numberparq = request.POST.get('numberparq', ''),
                    numberrows = request.POST.get('numberrows', '') ,
                )
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

            spaces = Spaces.objects.filter(parkinglot = parkinglot[0])
            spacesObj = []
            for obj in spaces:
                spacesObj.append({'name': obj.name, 'status' : obj.status, 'busy' : False})

            return JsonResponse({'success' : True, 'parkinglot': parkinglotObj, 'spaces' : spacesObj})
        else:
            return JsonResponse({'success' : False, 'parkinglot': {}, 'spaces' : []})

def parking(request):
    return render(request, 'parkings/index.html', {
        'title': 'Ingresos',
        'breadcrumb': ['Parqueos', 'Ingresos'],
        'parkings': jsonData()
    })

def postParking(request):
    success = True;
    message = "";
    if request.method == 'POST':
        # Primero buscamos si el vehiculo está registrado
        plate = request.POST.get('plateV').upper()
        spacesDisp = Spaces.objects.filter(plate = plate)

        print(spacesDisp, plate)

        if(spacesDisp.exists()):
            print(spacesDisp[0].income_at)
            History.objects.create(
                space = spacesDisp[0],
                plate = plate,
                income_at = spacesDisp[0].income_at,
                exit_at = timezone.now()
            )
            spacesDisp.update(
                busy = False,
                plate = "",
                exit_at = timezone.now()
            )            
            message = 'Se ha registrado la salida del vehículo'
        else:
            spacesDisp = Spaces.objects.filter(busy = False, status = True)
            if(spacesDisp.exists()):
                space = Spaces.objects.filter(id = spacesDisp.first().id)
                space.update(
                    busy = True,
                    plate = plate,
                    income_at = timezone.now()
                )
                message = 'Vehículo ingresado con éxito'
            else:
                message = 'No hay ningun espacio de parqueo disponible'
                success = False

        return JsonResponse({'success' : success, 'message': message, 'parkings': jsonData()})

def history(request):
    floors = Floors.objects.order_by('-created_at').all()
    return render(request, 'reports/history.html', {
        'title': 'Historial',
        'breadcrumb': ['Parqueos', 'Historial'],
        'floors': floors
    })

def getPLDetail(request):
    if request.method == 'POST':
        parkinglot = ParkingLots.objects.filter(floor = request.POST.get('floor', ''))
        if(parkinglot.exists()):
            spaces = Spaces.objects.filter(parkinglot = parkinglot[0])
            spacesObj = []
            for obj in spaces:
                spacesObj.append({'name': obj.name, 'status' : obj.status, 'id': obj.id})

            return JsonResponse({'success' : True, 'spaces' : spacesObj})
        else:
            return JsonResponse({'success' : False, 'spaces' : []})
        
def getSpaceHistory(request):
    if request.method == 'POST':
        history = History.objects.filter(space = request.POST.get('space', ''))
        if(history.exists()):
            historyObj = []
            for obj in history:
                historyObj.append({'plate': obj.plate, 'income_at' : obj.income_at, 'exit_at': obj.exit_at, 'diff' : obj.diferencia_fechas() })

            return JsonResponse({'success' : True, 'history' : historyObj})
        else:
            return JsonResponse({'success' : False, 'history' : []})

#Metodos auxiliares

def jsonData():
    parkinglots = ParkingLots.objects.all()
    parkingsJson = []

    for parkinglot in parkinglots:
        parking = {
            'name': parkinglot.name, 
            'floor': parkinglot.floor.name, 
            'numberparq': parkinglot.numberparq, 
            'numberrows': parkinglot.numberrows,
            'orientation': parkinglot.orientation,
            'status' : parkinglot.status,
            'spaces' : []
        }
        
        spaces = Spaces.objects.filter(parkinglot = parkinglot)
        spacesJson = []
        for space in spaces:
            spacesJson.append({'name': space.name, 'status' : space.status, 'busy': space.busy, 'plate' : space.plate})
        
        parking['spaces'] = spacesJson
        parkingsJson.append(parking)

    return json.dumps(parkingsJson, cls=DjangoJSONEncoder)