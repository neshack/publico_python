#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True) 
    cli_nombre = models.CharField(max_length=300)
    cli_correo = models.EmailField(max_length=180)
    cli_tel = models.CharField(max_length=75, blank=True)
    cli_cel = models.CharField(max_length=75, blank=True)
    cli_direccion = models.CharField(max_length=100, blank=True)
    cli_foto = models.ImageField(upload_to='clientes', verbose_name='Imágen')
    usu = models.ForeignKey(User)
    class Meta:
        db_table = u'cliente'
    def __unicode__(self):
    	return self.cli_nombre

class Cuenta(models.Model):
    cue_id = models.AutoField(primary_key=True)
    cue_nombre = models.CharField(max_length=300, blank=True)
    cue_fecha_alta = models.DateTimeField(null=True, blank=True)
    cli = models.ForeignKey(Cliente)
    class Meta:
        db_table = u'cuenta'
    def __unicode__(self):
    	return self.cue_nombre

class Dominio(models.Model):
    dom_id = models.AutoField(primary_key=True)
    dom_nombre = models.CharField(max_length=300)
    dom_fecha_alta = models.DateTimeField()
    dom_fecha_vencimiento = models.DateTimeField()
    dom_costo = models.DecimalField(max_digits=8, decimal_places=2)
    cue = models.ForeignKey(Cuenta)
    class Meta:
        db_table = u'dominio'

class Estadocuenta(models.Model):
    edc_id = models.AutoField(primary_key=True)
    edc_fecha = models.DateTimeField()
    edc_tipo_mov = models.IntegerField()
    edc_monto = models.CharField(max_length=135, blank=True)
    cli = models.ForeignKey(Cliente)
    class Meta:
        db_table = u'estadocuenta'

class Hosting(models.Model):
    hos_id = models.AutoField(primary_key=True)
    hos_fecha_registro = models.DateTimeField()
    hos_fecha_vencimiento = models.DateTimeField()
    hos_costo = models.DecimalField(max_digits=9, decimal_places=2)
    hos_servidor = models.CharField(max_length=300)
    hos_usuario = models.CharField(max_length=90)
    hos_contrasena = models.CharField(max_length=90)
    hos_plan = models.CharField(max_length=90, blank=True)
    cue = models.ForeignKey(Cuenta)
    class Meta:
        db_table = u'hosting'