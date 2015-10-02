from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    perfis = Perfil.objects.all()
    return render(request, 'index.html', { "perfis" : perfis })

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id = perfil_id);
    return render(request, 'perfil.html', { "perfil" : perfil })
