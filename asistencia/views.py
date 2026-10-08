from django.shortcuts import render, redirect
from .models import Asistencia

def listado(request):
    asistencias = Asistencia.objects.all()
    return render(request, "index.html", {"asistencias": asistencias})

def crear(request):
    if request.method == "POST":
        nuevo_registro = Asistencia(
            nombres=request.POST["nombres"],
            apellidos=request.POST["apellidos"],
            tipo_documento=request.POST["tipo_documento"],
            numero_documento=request.POST["numero_documento"],
            whatsapp=request.POST["whatsapp"],
            fecha=request.POST["fecha"],
            asistio=request.POST.get("asistio") == "true"
        )
        nuevo_registro.save()
        return redirect("/asistencia/")
    return render(request, "registrar.html")

def editar(request, id):
    editar_asistencia = Asistencia.objects.get(id=id)

    if request.method == "POST":
        editar_asistencia.nombres = request.POST["nombres"]
        editar_asistencia.apellidos = request.POST["apellidos"]
        editar_asistencia.tipo_documento = request.POST["tipo_documento"]
        editar_asistencia.numero_documento = request.POST["numero_documento"]
        editar_asistencia.whatsapp = request.POST["whatsapp"]
        editar_asistencia.fecha = request.POST["fecha"]
        editar_asistencia.asistio = request.POST.get("asistio") == "true"
        
        editar_asistencia.save()
        return redirect("/asistencia/")

    return render(
        request, "registrar.html", {"asistencia": editar_asistencia}
    )

def eliminar(request, id):
    eliminar_registro = Asistencia.objects.get(id=id)
    eliminar_registro.delete()
    return redirect("/asistencia/")