from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from venta.models import Recorrido, Pasaje


@require_GET
def indice(request):
    return render(request, "compra/indice.html")


@require_GET
def detalleC(request, id_recorrido):
    recorrido = get_object_or_404(Recorrido, id_recorrido=id_recorrido)
    pasajes = recorrido.pasaje_set.all()

    context = {
        'recorrido': recorrido,
        'asientos': pasajes,
    }

    return render(request, "compra/detalleC.html", context)


@require_GET
def buscarC(request):
    origen = request.GET.get("origen", "")
    destino = request.GET.get("destino", "")

    lista_recorridos = Recorrido.objects.filter(origen__nombre__contains=origen).\
        filter(destino__nombre__contains=destino)

    ctx = {'lista_recorridos': lista_recorridos}

    return render(request, "compra/buscarC.html", ctx)


@require_GET
def confirmarC(request, id_recorrido, sid_pasaje):
    recorrido = Recorrido.objects.get(id_recorrido=id_recorrido)
    asiento = Pasaje.objects.get(sid=sid_pasaje)

    if asiento.recorrido_id != recorrido.id_recorrido:
        raise Http404

    ctx = {
        'recorrido': recorrido,
        'asiento': asiento,
    }
    return render(request, "compra/confirmarC.html", ctx)


@require_POST
def comprar(request, sid_pasaje):
    try:
        pasaje = Pasaje.objects.get(sid=sid_pasaje)
        if pasaje.vendido:
            raise Http404
        pasaje.vendido = True

        pasaje.save()

        success_msg = "Pasaje comprado Exitosamente."

        #TODO: introducir mensaje de exito
        redirect = HttpResponse(mimetype='application/pdf')
        redirect['Content-Disposition'] = 'attachment; filename=boleto.pdf'
        p = canvas.Canvas(redirect)
        w, h = letter
        p.drawString(100,h-50, "Buses El Pintor")
        p.drawString(100,h-80, "Detalles de su Pasaje:")
        p.drawString(100,h-110,"Origen:")
        p.drawString(100+150,h-110, str(pasaje.recorrido.origen))
        p.drawString(100,h-140,"Hora salida:")
        p.drawString(100+150,h-140,str(pasaje.recorrido.hora_inicio))
        p.drawString(100,h-170,"Destino:")
        p.drawString(100+150,h-170,str(pasaje.recorrido.destino))
        p.drawString(100,h-200,"Hora llegada:")
        p.drawString(100+150,h-200,str(pasaje.recorrido.hora_llegada))
        p.drawString(100,h-230,"Bus asignado:")
        p.drawString(100+150,h-230,str(pasaje.recorrido.bus_asignado.patente))
        p.drawString(100,h-260,"Asiento")
        p.drawString(100+150,h-260,str(pasaje.asiento))
        p.drawString(100,h-350,"Gracias por preferirnos!")
        p.drawString(100,h-370,"Disfrute su viaje!")
        p.save()
        return redirect

    except IntegrityError:
        #TODO: Vista incorrecta!
        return render(request, "compra/confirmarC.html")





