from principal.models import *
from django.shortcuts import render_to_response

def lista_clientes(request):
	clientes = Cliente.objects.all()
	return render_to_response('lista_clientes.html',{'lista':clientes})

def lista_cuentas(request):
	cuentas = Cuenta.objects.all()
	return render_to_response('lista_cuentas.html',{'lista':cuentas})