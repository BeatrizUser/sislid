from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from cadastro.views import cadastrar_pessoa, sucesso

urlpatterns = [
    path('formulario/', cadastrar_pessoa, name='cadastrar_pessoa'),
    path('sucesso/', sucesso, name='sucesso'),
    path('admin/', admin.site.urls),
    path('gabineteonline/', include('gabineteOnline.urls')),
    path('blog/', include('blogZito.urls')),
    path('areacolaborador/', include('gabineteOnline.urls')),
    path('admin/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
