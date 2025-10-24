from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Facultys


def inicio1(request):
    listaFacultades = Facultys.objects.all()
    return render(request, "inicio1.html", {'facultades': listaFacultades})



def nuevaFacultad(request):
    return render(request, "Nuevo.html")


# Guardar nueva facultad
def GuardarFacultad(request):
    nombre_facultad = request.POST["nombre_facultad"]
    acronym_fac = request.POST.get("acronym_fac")
    dean_name_fac = request.POST.get("dean_name_fac")
    phone_fac = request.POST.get("phone_fac")
    email_fac = request.POST.get("email_fac")
    year_fundation_fac = request.POST.get("year_fundation_fac")

    logo_fac = request.FILES.get("logo_fac")

    nuevaFac = Facultys.objects.create(
        nombre_facultad=nombre_facultad,
        acronym_fac=acronym_fac,
        dean_name_fac=dean_name_fac,
        phone_fac=phone_fac,
        email_fac=email_fac,
        year_fundation_fac=year_fundation_fac,
        logo_fac=logo_fac
    )
    messages.success(request, "Facultad guardada correctamente")
    return redirect('/')


# Eliminar facultad
def EliminarFacultad(request, id):
    fac = get_object_or_404(Facultys, id=id)
    fac.delete()
    messages.success(request, "Facultad eliminada correctamente")
    return redirect('/')


# Editar facultad
def editarFacultad(request, id):
    fac = get_object_or_404(Facultys, id=id)
    return render(request, "Editar.html", {'facultad': fac})


# Guardar cambios en edición
def GuardarEdicionFacultad(request):
    id = request.POST["id"]
    nombre_facultad = request.POST["nombre_facultad"]
    acronym_fac = request.POST.get("acronym_fac")
    dean_name_fac = request.POST.get("dean_name_fac")
    phone_fac = request.POST.get("phone_fac")
    email_fac = request.POST.get("email_fac")
    year_fundation_fac = request.POST.get("year_fundation_fac")

    fac = get_object_or_404(Facultys, id=id)

    nuevo_logo = request.FILES.get("logo_fac")

    fac.nombre_facultad = nombre_facultad
    fac.acronym_fac = acronym_fac
    fac.dean_name_fac = dean_name_fac
    fac.phone_fac = phone_fac
    fac.email_fac = email_fac
    fac.year_fundation_fac = year_fundation_fac

    if nuevo_logo:
        fac.logo_fac = nuevo_logo

    fac.save()
    messages.success(request, "Facultad actualizada correctamente")
    return redirect('/')
