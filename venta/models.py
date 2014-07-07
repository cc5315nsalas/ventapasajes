from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return self.nombre


class Conductor(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s, rut=%s' % (self.nombre, self.rut)


class Bus(models.Model):
    patente = models.CharField(max_length=10, primary_key=True)
    capacidad = models.IntegerField()
    conductor = models.ForeignKey(Conductor, null=True)

    def __unicode__(self):
        return u'patente=%s, capacidad=%s, conducido por %s' % (self.patente, self.capacidad, self.conductor.nombre if self.conductor else "Nadie")


class Recorrido(models.Model):
    id_recorrido = models.AutoField(primary_key=True)
    origen = models.ForeignKey(Ciudad, related_name='ciudad_origen')
    destino = models.ForeignKey(Ciudad, related_name='ciudad_destino')
    hora_inicio = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    bus_asignado = models.ForeignKey(Bus, null=True, blank=True)

    def __unicode__(self):
        return u'%s -- %s\t\tsalida=%s' % (self.origen, self.destino, self.hora_inicio)


class Pasaje(models.Model):
    recorrido = models.ForeignKey(Recorrido)
    asiento = models.IntegerField()
    precio = models.IntegerField()
    vendido = models.BooleanField()
    sid = models.CharField(max_length=80, null=True)