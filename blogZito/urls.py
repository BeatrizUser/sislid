from django.urls import path
from blogZito import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]