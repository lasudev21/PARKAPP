from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        # 'data': categories
    })
