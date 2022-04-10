from django.shortcuts import render
from utils.curso.factory import make_cursos
from utils.cursos.factory import make_curso


# Create your views here.
def home(request):
    return render(request, 'cursos/pages/home.html', context={
        'cursos': make_cursos(),
    })


def curso(request, id):
    cursos = make_cursos()
    list_keys = [id]
    curso = list(filter(lambda d: d['id'] in list_keys, cursos))

    return render(request, 'cursos/pages/curso-view.html', context={
        'curso': curso[0],
        'is_detail_page': True,
    })


def cursos(request, id):
    return render(request, 'cursos/pages/curso-view.html', context={
        'curso': make_curso(),
        'is_detail_page': True,
    })
