from django.urls import path
from . import views

urlpatterns = [
    path('macieiras/pre-plantio/', views.Macieiras, name='Macieiras'),
    path('gramineas-leguminosas-frias/pre-plantio/', views.GramineasLeguminosasFrias, 
         name='Consorciações de Gramíneas e de Leguminosas de Estação Fria'),  
]