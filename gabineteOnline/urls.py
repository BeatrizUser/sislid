from django.urls import path
from gabineteOnline import views

urlpatterns = [
    path('perguntas/', views.perguntas, name='perguntas'),
]
