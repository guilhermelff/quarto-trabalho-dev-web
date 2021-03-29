from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'principal/index.html')


def explorar(request):
    return render(request, 'principal/explorar.html')


def expOnline(request):
    return render(request, 'principal/expOnline.html')


def sejaUmAnfitriao(request):
    return render(request, 'principal/sejaUmAnfitriao.html')
