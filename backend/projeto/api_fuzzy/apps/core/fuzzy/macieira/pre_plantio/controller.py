from typing import Tuple
from .fosforo_fuzzy import FosforoFuzzy
from .potassio_fuzzy import PotassioFuzzy
from ...calculos_gerais.calagem_calculo import Calcario

class CalculoFuzzy:

    def __init__(self, request):
        self.fosforo = request.data['fosforo']
        self.potassio = request.data['potassio']
        self.indice_smp = round(float(request.data['indice_smp']), 1)
        self.calcio = float(request.data['calcio'])
        self.magnesio = float(request.data['magnesio'])
        self.ctc = float(request.data['ctc'])
        self.argila = request.data['argila']
        self.areaPlantada = float(request.data['areaPlantada'])
        self.ph_agua = float(request.data['ph_agua'])

    def calcarioCalculo(self) -> Tuple[str, float, float]:
        ph_escolha = 6
        ph_desejado = 6.5
        sat_ca_min = 50 #em %
        sat_ca_max = 60 #em %
        sat_mg_min = 15 #em %
        sat_mg_max = 20 #em %

        calagem = Calcario.defineCalagem(
                    ph_agua=self.ph_agua,
                    area_plantada=self.areaPlantada,
                    indice_smp=self.indice_smp, 
                    ph_escolha=ph_escolha, 
                    ph_desejado=ph_desejado, 
                    ca_inicial=self.calcio, 
                    mg_inicial=self.magnesio, 
                    sat_ca_min=sat_ca_min,
                    sat_ca_max=sat_ca_max,
                    sat_mg_min=sat_mg_min, 
                    sat_mg_max=sat_mg_max,
                    ctc=self.ctc)
        
        return calagem

    def fosforoCalculo(self) -> Tuple[float, float]:
        p_quantidade_hectare: float
        p_quantidade_total: float

        p_quantidade_hectare = FosforoFuzzy.fazCalculo(self.argila, self.fosforo)
        p_quantidade_total = p_quantidade_hectare * self.areaPlantada 

        return p_quantidade_hectare, p_quantidade_total

    def potassioCalculo(self) -> Tuple[float, float]:
        k_quantidade_hectare: float
        k_quantidade_total: float

        k_quantidade_hectare = PotassioFuzzy.fazCalculo(self.ctc, self.potassio)
        k_quantidade_total = k_quantidade_hectare * self.areaPlantada 

        return k_quantidade_hectare, k_quantidade_total