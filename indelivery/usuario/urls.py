from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # em views vai ter uma função home
    path("cadastro", views.cadastrar, name='cadastro'), # nova view com a função para o cadastro
    path("login", views.login, name='login'), # nova view
    path("logout", views.logout, name='logout'), #view logout
]