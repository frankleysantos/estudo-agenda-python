from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar =True
    )
    paginacao = Paginator(contatos, 2)
    page_number = request.GET.get('p')
    contatos = paginacao.get_page(page_number)
    print(contatos)
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
