from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

class FosforoFuzzyG:
    def fazCalculo(argila_entrada: str, fosforo_entrada: str) -> float:
        #define universo
        x_argila = np.arange(4, 100, 1)
        x_teor_fosforo = np.arange(0, 70, 0.1)
        x_fosforo_por_ha  = np.arange(0, 250, 1)


        #define variaveis de entrada
        argila = ctrl.Antecedent(x_argila, 'teor_argila')
        teor_fosforo = ctrl.Antecedent(x_teor_fosforo, 'teor_fosforo')
        fosforo_por_ha = ctrl.Consequent(x_fosforo_por_ha, 'fosforo_saida')

        #funcoes de pertinencia das variaveis de entrada
        argila['faixa_1'] = fuzz.zmf(x_argila, 15, 25)
        argila['faixa_2'] = fuzz.trapmf(x_argila, [15, 25, 35, 45])
        argila['faixa_3'] = fuzz.trapmf(x_argila, [35, 45, 55, 65])
        argila['faixa_4'] = fuzz.smf(x_argila, 55, 65)

        teor_fosforo['muito_baixo'] = fuzz.zmf(x_teor_fosforo, 0, 3)
        teor_fosforo['baixo'] = fuzz.trimf(x_teor_fosforo, [3, 6, 9])
        teor_fosforo['pouco_baixo'] = fuzz.trimf(x_teor_fosforo, [6, 9, 12])
        teor_fosforo['medio'] = fuzz.trimf(x_teor_fosforo, [9, 15, 21])
        teor_fosforo['pouco_alto'] = fuzz.trimf(x_teor_fosforo, [15, 21, 27])
        teor_fosforo['alto'] = fuzz.trimf(x_teor_fosforo, [18, 30, 42])
        teor_fosforo['muito_alto'] = fuzz.smf(x_teor_fosforo, 36, 60)
        teor_fosforo['muito_muito_alto'] = fuzz.smf(x_teor_fosforo, 50, 70)

        # Definindo o sistema de regras
        rules = []
