from django.urls import path
from . import views

app_name = 'principal'
urlpatterns = [
    path('', views.index, name='index'),
    path('explorar', views.explorar, name='explorar'),
    path('expOnline', views.expOnline, name='expOnline'),
    path('sejaUmAnfitriao', views.sejaUmAnfitriao, name='sejaUmAnfitriao')
]
