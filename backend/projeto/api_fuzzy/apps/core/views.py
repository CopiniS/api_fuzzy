
from .fuzzy.macieira.pre_plantio.controller import CalculoFuzzy
from django.http import JsonResponse
from django.views import View

class MacieirasPrePlantio(View):
    def post(self, request):
        c = CalculoFuzzy(request)
        k_quantidade_hectare, k_quantidade_total = c.potassioCalculo()
        p_quantidade_hectare, p_quantidade_total = c.fosforoCalculo()

        response_data = {
            'k_quant_hec': k_quantidade_hectare,
            'k_quant_total': k_quant_total,
            'p_quant_hec': p_quantidade_hectare,
            'p_quant_total': p_quant_total,
        }

        return JsonResponse(response_data)

class GramineasLeguminosasFriasPrePlantio(View):
    def post(self, request):
        pass