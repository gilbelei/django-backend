from django.shortcuts import render

from .forms import RegisterForm


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'visitantes/pages/register_view.html', {
        'form': form,
    })
