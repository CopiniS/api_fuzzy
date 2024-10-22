from django.urls import path
from . import views

urlpatterns = [
    path('macieiras/', views.Macieiras, name='Macieiras'),
    path('gramineas-leguminosas-frias/', views.GramineasLeguminosasFrias, 
         name='Consorciações de Gramíneas e de Leguminosas de Estação Fria'),  
]