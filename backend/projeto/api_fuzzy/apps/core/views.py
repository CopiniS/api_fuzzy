
from .fuzzy.macieira.pre_plantio.controller import CalculoFuzzy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MacieirasPrePlantio(APIView):
    def post(self, request):
        c = CalculoFuzzy(request)
        
        cal_tipo, cal_quantidade_hectare, cal_quantidade_total = c.calcarioCalculo()
        k_quantidade_hectare, k_quantidade_total = c.potassioCalculo()
        p_quantidade_hectare, p_quantidade_total = c.fosforoCalculo()

        response_data = {
            'calcario': cal_tipo,
            'cal_quant_hec': cal_quantidade_hectare,
            'cal_quant_total': cal_quantidade_total,
            'k_quant_hec': k_quantidade_hectare,
            'k_quant_total': k_quantidade_total,
            'p_quant_hec': p_quantidade_hectare,
            'p_quant_total': p_quantidade_total,
        }

        return Response({
            "message" : "Calculos realizados com sucesso!",
            "dados": response_data,
        }, status=status.HTTP_200_OK )

class GramineasLeguminosasFriasPrePlantio(APIView):
    def post(self, request):
        pass