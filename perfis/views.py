from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    perfis = Perfil.objects.all()
    return render(request, 'index.html', { "perfis" : perfis })

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id = perfil_id);
    return render(request, 'perfil.html', { "perfil" : perfil })

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def get_perfil_logado(request):
   return Perfil.objects.get(id=1)
