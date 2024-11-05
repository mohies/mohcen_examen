from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.db.models import Avg
from .models import Televisor,Usuario,Votacion,CuentaBancaria

# Create your models here.

def index(request):
    return render(request, 'index.html') 

def voto(request, televisor_id):
    ultimo_voto = Votacion.objects.filter(televisor=televisor_id).select_related('usuario', 'televisor').order_by('-fecha_voto').first()
    return render(request, 'ultimo_voto.html', {'ultimo_voto': ultimo_voto})

def televisores_con_voto_bajo(request, usuario_id):
    televisores = Televisor.objects.filter(
        votacion__usuario_id=usuario_id,
        votacion__puntuacion__lt=3
    ).distinct().all()
    
    return render(request, 'televisores_con_voto_bajo.html', {'televisores': televisores})


def usuarios_no(request):
    usuarios=Usuario.objects.filter(votacion=None).select_related('cuentabancaria').all()
    return render(request, 'usuarios_novotado.html', {'usuarios': usuarios})

def cuentas_bancarias_juan(request):
    cuentas = CuentaBancaria.objects.filter(Q(usuario__nombre__icontains="Juan") & (Q(banco="Caixa") | Q(banco="UNICAJA")))   
    return render(request, 'cuentas_bancarias_juan.html', {'cuentas': cuentas})


def votos_filtrados(request):
  votos = Votacion.objects.filter(Q(fecha_voto__year__gte=2023) &  Q(puntuacion=5) & Q(usuario__cuentabancaria__id__gt=2)).prefetch_related('usuario','televisor').all()
  return render(request, 'votos_filtrados.html', {'votos': votos})


def media(request):
    resultado = Televisor.objects.aggregate(Avg('votacion__puntuacion'))
    media = resultado['votacion__puntuacion__avg']
    return render(request, 'resultado_media.html', {'media': media})











def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)