from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('',            views.inicio, name='inicio' ),
    path('portafolio/', views.portafolio, name='portafolio' ),
    path('contacto/',   views.contacto, name='contacto' ),
    path('post/',        include('post.urls')),
]
