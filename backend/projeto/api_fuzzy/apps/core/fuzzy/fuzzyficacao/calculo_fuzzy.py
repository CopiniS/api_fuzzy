from typing import Tuple

class CalculoFuzzy:

    def __init__(self, planta: str):
        self.regras = ControllerRegras.retornaRegras(planta)


    def calcarioCalculo() -> Tuple[str, float, float]:
        calcario_tipo: str
        calcario_quantidade_hectare: float
        calcario_quantidade_total: float

        #aqui fazer a lógica do calculo chamando as regras
        
        return calcario_tipo, calcario_quantidade_hectare, calcario_quantidade_total

    def nitrogenioCalculo() -> Tuple[float, float]:
        n_quantidade_hectare: float
        n_quantidade_total: float

        #aqui fazer a lógica do calculo chamando as regras

        return n_quantidade_hectare, n_quantidade_total

    def fosforoCalculo() -> Tuple[float, float]:
        p_quantidade_hectare: float
        p_quantidade_total: float

        #aqui fazer a lógica do calculo chamando as regras

        return p_quantidade_hectare, p_quantidade_total

    def potassioCalculo() -> Tuple[float, float]:
        k_quantidade_hectare: float
        k_quantidade_total: float

        #aqui fazer a lógica do calculo chamando as regras

        return k_quantidade_hectare, k_quantidade_total