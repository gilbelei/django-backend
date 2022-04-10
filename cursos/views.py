from django.shortcuts import get_list_or_404, get_object_or_404, render

from cursos.models import Curso


# Create your views here.
def home(request):
    cursos = Curso.objects.filter(
        is_published=True,
    ).order_by('id')

    return render(request, 'cursos/pages/home.html', context={
        'cursos': cursos,
        'is_detail_page': False,
    })


def curso(request, id):
    curso = get_object_or_404(Curso, pk=id, is_published=True,)

    return render(request, 'cursos/pages/curso-view.html', context={
        'curso': curso,
        'is_detail_page': True,
    })


def categoria(request, categoria_id):
    cursos = get_list_or_404(
        Curso.objects.filter(
            categoria__id=categoria_id,
            is_published=True,
        ).order_by('id')
    )

    return render(request, 'cursos/pages/categoria.html', context={
        'cursos': cursos,
        'title': f'{cursos[0].categoria.name} - {cursos[0].categoria.type} | '
    })
