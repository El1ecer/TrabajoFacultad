from django.shortcuts import render, redirect
from Aplicaciones.Career.models import Careers
from .models import Teachings
from django.contrib import messages

def indexTeacher(request):
    listaDocentes = Teachings.objects.all()
    for d in listaDocentes:
        print(d.id, d.first_name)
    return render(request, 'inicio.html', {'docentes': listaDocentes})

def nuevoDocente(request):
    listaCarreras = Careers.objects.all()
    return render(request, 'nuevoD.html', {'carreras': listaCarreras})

def guardarDocente(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age') or None
        email = request.POST.get('email') or None
        carrera_id = request.POST.get('carrera')
        logo = request.FILES.get('logo')
        pdf = request.FILES.get('pdf')

        carrera = None
        if carrera_id:
            try:
                carrera = Careers.objects.get(id=carrera_id)
            except Careers.DoesNotExist:
                carrera = None

        Teachings.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            carrera=carrera,
            logo=logo,
            pdf=pdf
        )

        messages.success(request, 'Docente agregado correctamente')
        return redirect('/Teaching/')  

def editarDocente(request, id):
    try:
        docente = Teachings.objects.get(id=id)
    except Teachings.DoesNotExist:
        messages.error(request, 'Docente no encontrado')
        return redirect('/Teaching/')

    listaCarreras = Careers.objects.all()
    return render(request, 'editarD.html', {'docenteTemp': docente, 'carreras': listaCarreras})

def guardarEdicionDocente(request):
    if request.method == 'POST':
        idDocente = request.POST.get('id')
        try:
            docente = Teachings.objects.get(id=idDocente)
        except Teachings.DoesNotExist:
            messages.error(request, 'Docente no encontrado')
            return redirect('/Teaching/')

        docente.first_name = request.POST.get('first_name')
        docente.last_name = request.POST.get('last_name')
        docente.age = request.POST.get('age') or None
        docente.email = request.POST.get('email') or None

        carrera_id = request.POST.get('carrera')
        if carrera_id:
            try:
                docente.carrera = Careers.objects.get(id=carrera_id)
            except Careers.DoesNotExist:
                docente.carrera = None

        if 'logo' in request.FILES:
            docente.logo = request.FILES['logo']
        if 'pdf' in request.FILES:
            docente.pdf = request.FILES['pdf']

        docente.save()
        messages.success(request, 'Docente editado con éxito')
        return redirect('/Teaching/')

    else:
        return redirect('/Teaching/')

def eliminarDocente(request, id):
    try:
        docenteTemp = Teachings.objects.get(id=id)
        docenteTemp.delete()
        messages.success(request, 'Docente eliminado correctamente')
    except Teachings.DoesNotExist:
        messages.error(request, 'Docente no encontrado')
    
    return redirect('/Teaching/')
