from typing import Tuple
from .fosforo_fuzzy import FosforoFuzzy
from .potassio_fuzzy import PotassioFuzzy
from ...calculos_gerais.calagem_calculo import Calcario

class CalculoFuzzy:

    def __init__(self, request):
        self.fosforo = request.data['fosforo']
        self.potassio = request.data['potassio']
        self.indice_smp = request.data['indice_smp']
        self.calcio = request.data['calcio']
        self.magnesio = request.data['magnesio']
        self.ctc = request.data['ctc']
        self.argila = request.data['argila']
        self.areaPlantada = float(request.data['areaPlantada'])

    def calcarioCalculo(self) -> Tuple[str, float, float]:
        calcario_tipo: str
        calcario_quantidade_hectare: float
        calcario_quantidade_total: float
        ph_escolha = 6
        ph_desejado = 6.5
        sat_ca_min = 50 #em %
        sat_ca_max = 60 #em %
        sat_mg_min = 15 #em %
        sat_mg_max = 20 #em %


        calcario_quantidade_hectare = Calcario.fazCalculo(float(self.indice_smp), ph_escolha, ph_desejado) * 1000  # vezes 1000 para deixar em kg
        calcario_quantidade_total = calcario_quantidade_hectare * self.areaPlantada / 10000  # divide por 1000 para deixar em hectare
        

        # calcario_tipo = 'Calcário Calcítico' #EM MACIEIRAS È MELHOR NAO TER MG NA CALAGEM
        calcario_tipo = Calcario.escolheTipoMisto(calcario_quantidade_hectare, 
                                                    self.calcio, 
                                                    self.magnesio, 
                                                    sat_ca_min,
                                                    sat_ca_max,
                                                    sat_mg_min, 
                                                    sat_mg_max,
                                                    self.ctc)
        
        return calcario_tipo, calcario_quantidade_hectare, calcario_quantidade_total

    def fosforoCalculo(self) -> Tuple[float, float]:
        p_quantidade_hectare: float
        p_quantidade_total: float

        p_quantidade_hectare = FosforoFuzzy.fazCalculo(self.argila, self.fosforo)
        p_quantidade_total = p_quantidade_hectare * self.areaPlantada / 10000

        return p_quantidade_hectare, p_quantidade_total

    def potassioCalculo(self) -> Tuple[float, float]:
        k_quantidade_hectare: float
        k_quantidade_total: float

        k_quantidade_hectare = PotassioFuzzy.fazCalculo(self.ctc, self.potassio)
        k_quantidade_total = k_quantidade_hectare * self.areaPlantada / 10000

        return k_quantidade_hectare, k_quantidade_total