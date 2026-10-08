from django.shortcuts import render, redirect
from .models import Asistencia

# Create your views here.

def listado(request):
    asistencias = Asistencia.objects.all()
    return render(
        request, "index.html", {"asistencias" : asistencias}
    )

def crear(request):
    if request.method == "POST":
        nuevo_registro = Asistencia(
            nombres = request.POST["nombres"],
            apellidos = request.POST["apellidos"],
            tipo_documento = request.POST["tipo_documento"],
            numero_documento = request.POST["numero_documento"],
            whatsapp = request.POST["whatsapp"],
            fecha = request.POST["fecha"],
            asistio = request.POST["asistio"]
        )
        nuevo_registro.save()
        return redirect("/asistencia/")
    return render(request, "registrar.html")