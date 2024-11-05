from django.urls import path
from . import views

urlpatterns = [
    path('macieiras/pre-plantio/', views.MacieirasPrePlantio.as_view(), name='MacieirasPrePlantio'),
    path('gramineas-leguminosas-frias/pre-plantio/', views.GramineasLeguminosasFriasPrePlantio.as_view(), 
         name='Consorciações de Gramíneas e de Leguminosas de Estação Fria em Pré plantio'),  
]