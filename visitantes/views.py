from django.shortcuts import render


def register_view(request):
    return render(request, 'visitantes/pages/register_view.html')
