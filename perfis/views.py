from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil();

    if perfil_id == '1':
        perfil = Perfil('Leandro', 'leandro@leandro.com', '878787799', 'HU')

    return render(request, 'perfil.html', { "perfil" : perfil })
