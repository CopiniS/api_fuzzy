from typing import Tuple
from fosforo_fuzzy import FosforoFuzzy
from potassio_fuzzy import PotassioFuzzy

class CalculoFuzzy:

    def __init__(self, 
                 areaPlantada: float,
                 fosforo: float,
                 potassio: float,
                 calcario: float,
                 ctc: float,
                 argila: float,):
        self.fosforo = fosforo
        self.potassio = potassio
        self.calcario = calcario
        self.ctc = ctc
        self.argila = argila

    def calcarioCalculo() -> Tuple[str, float, float]:
        calcario_tipo: str
        calcario_quantidade_hectare: float
        calcario_quantidade_total: float

        #aqui fazer a lógica do calculo chamando as regras
        
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