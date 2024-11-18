
from .fuzzy.macieira.pre_plantio.controllerM import CalculoFuzzyM
from .fuzzy.gramineas_leguminosas_frias.pre_plantio.controllerG import CalculoFuzzyG
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MacieirasPrePlantio(APIView):
    def post(self, request):
        c = CalculoFuzzyM(request)
        
        calagem = c.calcarioCalculoM()
        k_quantidade_hectare, k_quantidade_total = c.potassioCalculoM()
        p_quantidade_hectare, p_quantidade_total = c.fosforoCalculoM()

        response_data = {
            'k_quant_hec': k_quantidade_hectare,
            'k_quant_total': k_quantidade_total,
            'p_quant_hec': p_quantidade_hectare,
            'p_quant_total': p_quantidade_total,
            'calagem': calagem
        }

        return Response({
            "message" : "Calculos realizados com sucesso!",
            "dados": response_data,
        }, status=status.HTTP_200_OK )

class GramineasLeguminosasFriasPrePlantio(APIView):
    def post(self, request):
        c = CalculoFuzzyG(request)

        calagem = c.calcarioCalculoG()
        k_quantidade_hectare, k_quantidade_total = c.potassioCalculoG()
        p_quantidade_hectare, p_quantidade_total = c.fosforoCalculoG()

        response_data = {
            'k_quant_hec': k_quantidade_hectare,
            'k_quant_total': k_quantidade_total,
            'p_quant_hec': p_quantidade_hectare,
            'p_quant_total': p_quantidade_total,
            'calagem': calagem
        }
        return Response({
            "message" : "Calculos realizados com sucesso!",
            "dados": response_data,
        }, status=status.HTTP_200_OK )
