from django.urls import path
from gabineteOnline import views

urlpatterns = [
    path('perguntas/', views.perguntas, name='perguntas'),
    path('formulario/', views.formulario, name='formulario'),
]
