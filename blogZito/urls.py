from django.urls import path
from blogZito import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('propostas/', views.propostas, name='propostas'),
    path('', views.blog, name='blog'),
    path('post<int:post_id>/', views.post_detail, name='post_detail'),
]