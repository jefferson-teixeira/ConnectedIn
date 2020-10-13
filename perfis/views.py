from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite

# Create your views here.
def index(request):
    return render(
        request,
        'index.html', 
        {
            'perfis': Perfil.objects.all(),
            'perfil_logado': obter_perfil_logado(request)
        }
    )


def exibir_perfil(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)
    perfil_logado = obter_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(
        request,
        'perfil.html',
        {
            'perfil': perfil,
            'perfil_logado': perfil_logado,
            'ja_eh_contato': ja_eh_contato
        }
    )


def convidar(request, id_perfil):
    perfil_para_convidar = Perfil.objects.get(id=id_perfil)
    perfil_logado = obter_perfil_logado(request)
    perfil_logado.convidar(perfil_para_convidar)
    return redirect('index')


def obter_perfil_logado(request):
    return Perfil.objects.get(id=1)


def aceitar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.aceitar()
    return redirect('index')
