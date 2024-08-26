
#from django.contrib import admin
from django.urls import path
from app_cadastro_fornecedores import views

urlpatterns = [
    # rota, view resposável, nome de refêrencia.
    #fornecedores.com
    path('', views.home,
     name='home'),

]
