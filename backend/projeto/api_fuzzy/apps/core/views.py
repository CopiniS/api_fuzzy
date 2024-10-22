from core import models

class Amostra:
    # Análise de Solo
    materia_organica: float
    ph: float
    fosforo: float
    potassio: float
    calcio: float
    magnesio: float
    boro: float 
    zinco: float 
    saturacao_bases: float
    ctc_cmol: float

    # Análise Foliar
    nitrogenio_foliar: float
    fosforo_foliar: float
    potassio_foliar: float
    calcio_foliar: float
    magnesio_foliar: float
    
    ferro_foliar: float
    cobre_foliar: float
    zinco_foliar: float
    manganes_foliar: float
    boro_foliar: float

    # Outros Parâmetros
    produtividade: float
    crescimento_ramos: int

    def __init__(self, materia_organica: float, ph: float, fosforo: float, potassio: float,
                 calcio: float, magnesio: float, saturacao_bases: float, ctc_cmol: float,
                 nitrogenio_foliar: float, fosforo_foliar: float, potassio_foliar: float,
                 calcio_foliar: float, magnesio_foliar: float, ferro_foliar: float, cobre_foliar: float,
                 zinco_foliar: float, manganes_foliar: float, boro_foliar: float, produtividade: float,
                 crescimento_ramos: int, boro: float = 0.0, zinco: float = 0.0):
        # Atribuição dos valores às propriedades da classe
        self.materia_organica = materia_organica
        self.ph = ph
        self.fosforo = fosforo
        self.potassio = potassio
        self.calcio = calcio
        self.magnesio = magnesio
        self.boro = boro
        self.zinco = zinco
        self.saturacao_bases = saturacao_bases
        self.ctc_cmol = ctc_cmol

        self.nitrogenio_foliar = nitrogenio_foliar
        self.fosforo_foliar = fosforo_foliar
        self.potassio_foliar = potassio_foliar
        self.calcio_foliar = calcio_foliar
        self.magnesio_foliar = magnesio_foliar

        self.ferro_foliar = ferro_foliar
        self.cobre_foliar = cobre_foliar
        self.zinco_foliar = zinco_foliar
        self.manganes_foliar = manganes_foliar
        self.boro_foliar = boro_foliar

        self.produtividade = produtividade
        self.crescimento_ramos = crescimento_ramos
 
class Analise:
    calcario_tipo: str
    calcario_quantidade_hectare: float
    calcario_quantidade_total: float
    n_quantidade_hectare: float
    n_quantidade_total: float
    p_quantidade_hectare: float
    p_quantidade_total: float
    k_quantidade_hectare: float
    k_quantidade_total: float

    def __init__(self, calcario_tipo: str, calcario_quantidade_hectare: float, calcario_quantidade_total: float,
                 n_quantidade_hectare: float, n_quantidade_total: float,
                 p_quantidade_hectare: float, p_quantidade_total: float,
                 k_quantidade_hectare: float, k_quantidade_total: float):
        self.calcario_tipo = calcario_tipo
        self.calcario_quantidade_hectare = calcario_quantidade_hectare
        self.calcario_quantidade_total = calcario_quantidade_total
        self.n_quantidade_hectare = n_quantidade_hectare
        self.n_quantidade_total = n_quantidade_total
        self.p_quantidade_hectare = p_quantidade_hectare
        self.p_quantidade_total = p_quantidade_total
        self.k_quantidade_hectare = k_quantidade_hectare
        self.k_quantidade_total = k_quantidade_total

class Macieiras(self):
    def post(self, request):
        #Aqui será a lógica fuzzy para macieiras
        #receberá os dados como está na classe Amostra
        #retornará os dados como está na classe Analise
        pass

class GramineasLeguminosasFrias:
    def post(self, request):
        #Aqui será a lógica fuzzy para gramineas_leguminosas
        #receberá os dados como está na classe Amostra
        #retornará os dados como está na classe Analise
        pass