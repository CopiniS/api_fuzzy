from typing import Tuple
from .fosforo_fuzzyM import FosforoFuzzyM
from .potassio_fuzzyM import PotassioFuzzyM
from ...calculos_gerais.calagem_calculo import Calcario

class CalculoFuzzyM:

    def __init__(self, request):
        self.fosforo = request.data['fosforo']
        self.potassio = request.data['potassio']
        self.indice_smp = float(request.data['indice_smp'])
        self.calcio = float(request.data['calcio'])
        self.magnesio = float(request.data['magnesio'])
        self.ctc = float(request.data['ctc'])
        self.argila = request.data['argila']
        self.areaPlantada = float(request.data['areaPlantada'])

    def calcarioCalculoM(self) -> Tuple[str, float, float]:
        ph_escolha = 6
        ph_desejado = 6.5
        sat_ca_min = 50 #em %
        sat_ca_max = 60 #em %
        sat_mg_min = 15 #em %
        sat_mg_max = 20 #em %

        calagem = Calcario.defineCalagem(
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

    def fosforoCalculoM(self) -> Tuple[float, float]:
        p_quantidade_hectare: float
        p_quantidade_total: float

        p_quantidade_hectare = FosforoFuzzyM.fazCalculo(self.argila, self.fosforo)
        p_quantidade_total = p_quantidade_hectare * self.areaPlantada 

        return p_quantidade_hectare, p_quantidade_total

    def potassioCalculoM(self) -> Tuple[float, float]:
        k_quantidade_hectare: float
        k_quantidade_total: float

        k_quantidade_hectare = PotassioFuzzyM.fazCalculo(self.ctc, self.potassio)
        k_quantidade_total = k_quantidade_hectare * self.areaPlantada 

        return k_quantidade_hectare, k_quantidade_total