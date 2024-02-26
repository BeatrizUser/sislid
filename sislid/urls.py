from django.contrib import admin
from django.urls import path
from cadastro import views  # Importe as views do seu aplicativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perguntas/', views.perguntas, name='perguntas'),  # Adicione esta linha para a nova view
]
