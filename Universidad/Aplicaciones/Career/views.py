from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Careers
from Aplicaciones.Faculty.models import Facultys  




def inicio2(request):
    lista_carreras = Careers.objects.select_related('facultad').all()
    return render(request, "inicio2.html", {
        'careers': lista_carreras   
    })



def nuevaCarrera(request):
    facultades = Facultys.objects.all()
    return render(request, "NewCareer.html", {
        'facultades': facultades
    })



def GuardarCarrera(request):
    facultad_id = request.POST.get("facultad")  
    name_career = request.POST.get("name_career")
    directory_car  = request.POST.get("directory_car")
    duration_years = request.POST.get("duration_years")
    phone_car = request.POST.get("phone_car")
    email_car = request.POST.get("email_car")
    logo = request.FILES.get("logo")

    nueva = Careers.objects.create(
        facultad_id=facultad_id,
        name_career=name_career,
        directory_car=directory_car,
        duration_years=duration_years if duration_years else None,
        phone_car=phone_car,
        email_car=email_car,
        logo=logo,
    )

    messages.success(request, "Carrera guardada correctamente")
    return redirect('/')  



def EliminarCarrera(request, id):
    car = get_object_or_404(Careers, id=id)
    car.delete()
    messages.success(request, "Carrera eliminada correctamente")
    return redirect('/')



def editarCarrera(request, id):
    car = get_object_or_404(Careers, id=id)
    facultades = Facultys.objects.all()
    return render(request, "EditCareer.html", {
        'career': car,
        'facultades': facultades
    })



def GuardarEdicionCarrera(request):
    id = request.POST.get("id")

    car = get_object_or_404(Careers, id=id)

    car.facultad_id   = request.POST.get("facultad")
    car.name_career   = request.POST.get("name_career")
    car.directory_car = request.POST.get("directory_car")
    duration_years    = request.POST.get("duration_years")
    car.duration_years = duration_years if duration_years else None
    car.phone_car     = request.POST.get("phone_car")
    car.email_car     = request.POST.get("email_car")

    # Archivos (solo si envían uno nuevo)
    nuevo_logo = request.FILES.get("logo")
    if nuevo_logo:
        car.logo = nuevo_logo

    car.save()
    messages.success(request, "Carrera actualizada correctamente")
    # return redirect('inicioCareer')
    return redirect('/')
