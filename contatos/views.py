from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator # paginação
from django.db.models import Q, Value #Usado para realizar consultas mais complexas
from django.db.models.functions import Concat # concatenação de campos
# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar =True
    )
    paginacao = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginacao.get_page(page_number)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404() # raise levanta o erro nesse caso

    campos = Concat('nome', Value(' '), 'sobrenome') # campos existentes base dados
    # contatos = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains= termo) | Q(sobrenome__icontains= termo), # like nome ou sobrenome
    #     mostrar =True,
    # )
    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    ).order_by('nome')
    paginacao = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginacao.get_page(page_number)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
