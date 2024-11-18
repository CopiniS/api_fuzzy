from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

class PotassioFuzzyM:

    def fazCalculo(ctc_entrada: str, potassio_entrada: str) -> float:
        #define universo
        x_ctc = np.arange(5, 40, 1)
        x_teor_potassio = np.arange(0, 500, 1)
        x_potassio_por_ha  = np.arange(0, 150, 1)

        #define variaveis de entrada
        ctc = ctrl.Antecedent(x_ctc, 'ctc')
        teor_potassio = ctrl.Antecedent(x_teor_potassio, 'teor_potassio')
        potassio_por_ha = ctrl.Consequent(x_potassio_por_ha, 'potassio_saida')

        #funcoes de pertinencia das variaveis de entrada
        ctc['faixa_1'] = fuzz.zmf(x_ctc, 6, 9)
        ctc['faixa_2'] = fuzz.trapmf(x_ctc, [6.1, 9.1, 13, 17])
        ctc['faixa_3'] = fuzz.trapmf(x_ctc, [13.1, 17.1, 26, 33])
        ctc['faixa_4'] = fuzz.smf(x_ctc,26.1,33.1)

        teor_potassio['muito_baixo'] = fuzz.zmf(x_teor_potassio, 20, 30)
        teor_potassio['baixo'] = fuzz.trapmf(x_teor_potassio, [20, 30, 40, 50])
        teor_potassio['pouco_baixo'] = fuzz.trapmf(x_teor_potassio, [40, 50, 60, 70])
        teor_potassio['medio'] = fuzz.trapmf(x_teor_potassio, [60, 70, 90, 100])
        teor_potassio['pouco_alto'] = fuzz.trapmf(x_teor_potassio, [90, 100, 110, 120])
        teor_potassio['alto'] = fuzz.trapmf(x_teor_potassio, [110, 120, 160, 180])
        teor_potassio['muito_alto'] = fuzz.trapmf(x_teor_potassio, [160, 200, 250, 270])
        teor_potassio['muito_muito_alto'] = fuzz.smf(x_teor_potassio, 250, 270)

        potassio_por_ha['muito_baixo'] = fuzz.zmf(x_potassio_por_ha, 20, 40)
        potassio_por_ha['baixo'] = fuzz.trapmf(x_potassio_por_ha, [20, 40, 60, 80])
        potassio_por_ha['medio'] = fuzz.trapmf(x_potassio_por_ha, [60, 80, 90, 110])
        potassio_por_ha['alto'] = fuzz.trapmf(x_potassio_por_ha, [90, 110, 130, 140])
        potassio_por_ha['muito_alto'] = fuzz.trapmf(x_potassio_por_ha, [130, 140, 150, 150])

        rules = [
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['muito_baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['baixo'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['pouco_baixo'], potassio_por_ha['medio']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['medio'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['pouco_alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['alto'], potassio_por_ha['muito_baixo']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['muito_alto'], potassio_por_ha['muito_baixo']),
            ctrl.Rule(ctc['faixa_1'] & teor_potassio['muito_muito_alto'], potassio_por_ha['muito_baixo']),

            ctrl.Rule(ctc['faixa_2'] & teor_potassio['muito_baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['baixo'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['pouco_baixo'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['medio'], potassio_por_ha['medio']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['pouco_alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['muito_alto'], potassio_por_ha['muito_baixo']),
            ctrl.Rule(ctc['faixa_2'] & teor_potassio['muito_muito_alto'], potassio_por_ha['muito_baixo']),

            ctrl.Rule(ctc['faixa_3'] & teor_potassio['muito_baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['pouco_baixo'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['medio'], potassio_por_ha['medio']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['pouco_alto'], potassio_por_ha['medio']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['muito_alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_3'] & teor_potassio['muito_muito_alto'], potassio_por_ha['muito_baixo']),

            ctrl.Rule(ctc['faixa_4'] & teor_potassio['muito_baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['baixo'], potassio_por_ha['muito_alto']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['pouco_baixo'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['medio'], potassio_por_ha['alto']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['pouco_alto'], potassio_por_ha['medio']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['muito_alto'], potassio_por_ha['baixo']),
            ctrl.Rule(ctc['faixa_4'] & teor_potassio['muito_muito_alto'], potassio_por_ha['muito_baixo'])
        ]

        # Criar o sistema de controle fuzzy
        potassio_ctrl = ctrl.ControlSystem(rules)
        potassio_sim = ctrl.ControlSystemSimulation(potassio_ctrl)


        # Definir as entradas para a simulação
        potassio_sim.input['ctc'] = float(ctc_entrada)  # Exemplo de valor de CTC
        potassio_sim.input['teor_potassio'] = float(potassio_entrada)  # Exemplo de valor de potássio

        # Calcular a saída
        potassio_sim.compute()

        # Obter e exibir o resultado
        resultado = potassio_sim.output['potassio_saida']  # Verificar o tipo do resultado)

        return resultado