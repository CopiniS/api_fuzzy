from gramineas_leguminosas_regras import GramineasLeguminosasRegras
from macieira_regras import MacieiraRegras


class ControllerRegras:
    def __init__(self):
        self.macieira = MacieiraRegras.retornaRegras()
        self.gramineas_leguminosas = GramineasLeguminosasRegras.retornaRegras()

    def retornaRegras(self, planta: str) -> dict:
        match planta.lower():
            case 'macieira':
                return self.macieira
            case 'gramineas_leguminosas':
                return self.gramineas_leguminosas

    