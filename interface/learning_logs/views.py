from django.shortcuts import render
import json
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Us, Tipo, Distrito, Concelho, Freguesia, Gruposintomas, Opcoesintomas
from .forms import USForm, TipoForm, DistritoForm, ConcelhoForm, FreguesiaForm, GruposintomasForm, OpcoesintomasForm

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def sobre(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/sobre.html')

def ped_anterior(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/historial.html')

def rec_rapida(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/recomendacao_rapida.html')

def edit_rec(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/edit_recomendacoes.html')

def edit_rec1(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/edit_recomendacoes1.html')

def us(request):
    context = {'us': us}
    return render(request, 'learning_logs/us.html', context)

def tipo_loc(request):
    """Show a single topic and all its entries."""
    tipos = Tipo.objects.all()
    distritos = Distrito.objects.all()
    context = {'tipos': tipos, 'distritos': distritos}
    return render(request, 'learning_logs/us_loc.html', context)

def tipo(request):
    """Show a single topic and all its entries."""
    tipos = Tipo.objects.all()
    distritos = Distrito.objects.all()
    context = {'tipos': tipos, 'distritos': distritos}
    return render(request, 'learning_logs/us.html', context)


def get_concelho(request):
    request.POST.get('CSRF')
    distritos_name = request.POST.get('dst')
    if distritos_name is None:
        return HttpResponseBadRequest()
    print ("ajax distritos_name ", distritos_name)

    result_set=Concelho.objects.filter(distrito__distrito__contains=distritos_name)
    context = {}
    for c in result_set:
        context[c.id] = c.concelho
    print(json.dumps(context))
    return HttpResponse(json.dumps(context), content_type="application/json")

def get_freguesia(request):
    request.POST.get('CSRF')
    concelhos_name = request.POST.get('ccl')
    if concelhos_name is None:
        return HttpResponseBadRequest()
    print ("ajax concelhos_name ", concelhos_name)

    result_set=Freguesia.objects.filter(concelho__concelho__contains=concelhos_name)
    context = {}
    for f in result_set:
        context[f.id] = f.freguesia
    print(json.dumps(context))
    return HttpResponse(json.dumps(context), content_type="application/json")

def get_loc(request):
    request.POST.get('CSRF')
    freguesias_name = request.POST.get('fgs')
    tipos_name = request.POST.get('tp')
    if freguesias_name is None:
        return HttpResponseBadRequest()
    if tipos_name is None:
        return HttpResponseBadRequest()
    print ("ajax tipos_name ", tipos_name)
    print ("ajax freguesias_name ", freguesias_name)

    result_set=Us.objects.filter(freguesia__freguesia__contains=freguesias_name, tipo__tipo__contains=tipos_name)
    context = {}
    for f in result_set:
        context[f.id] = f.unidade
    print(json.dumps(context))
    return HttpResponse(json.dumps(context), content_type="application/json")

def get_opcao(request):
    request.POST.get('CSRF')
    grupos_name = request.POST.get('grp')
    if grupos_name is None:
        return HttpResponseBadRequest()
    
    print ("ajax grupo_name ", grupos_name)
    result_set=Opcoesintomas.objects.filter(grupo__gruposintomas__contains=grupos_name)
    context = {}
    for f in result_set:
        context[f.id] = f.opcoes
    print(json.dumps(context))
    return HttpResponse(json.dumps(context), content_type="application/json")


def sint_rapida(request):
    gruposintomas = Gruposintomas.objects.all()
    tipos = Tipo.objects.all()
    #concelhos = Concelho.objects.all()
    #freguesias = Freguesia.objects.all()
    context = {'gruposintomass': gruposintomas, 'tipos': tipos}#, 'concelhos': concelhos, 'freguesias': freguesias}
    return render(request, 'learning_logs/sint_rapida.html', context)

def edit_sint(request):
    gruposintomas = Gruposintomas.objects.all()
    tipos = Tipo.objects.all()
    context = {'gruposintomass': gruposintomas, 'tipos': tipos}
    return render(request, 'learning_logs/edit_sint.html', context)

def new_sint(request):
    gruposintomas = Gruposintomas.objects.all()
    tipos = Tipo.objects.all()
    context = {'gruposintomass': gruposintomas, 'tipos': tipos}
    return render(request, 'learning_logs/new_sint.html', context)


@login_required
def menu(request):
    """Show a single topic and all its entries."""
   
    return render(request, 'learning_logs/menu.html')

