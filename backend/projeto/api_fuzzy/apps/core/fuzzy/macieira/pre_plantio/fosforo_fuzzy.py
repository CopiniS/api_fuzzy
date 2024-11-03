from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

class FosforoFuzzy:

    def fazCalculo(argila_entrada, fosforo_entrada) -> float:
        #define universo
        x_argila = np.arange(4, 100, 1)
        x_teor_fosforo = np.arange(0, 100, 1)
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

        teor_fosforo['muito_baixo'] = fuzz.zmf(x_teor_fosforo, 20, 30)
        teor_fosforo['baixo'] = fuzz.trapmf(x_teor_fosforo, [20, 30, 40, 50])
        teor_fosforo['pouco_baixo'] = fuzz.trapmf(x_teor_fosforo, [40, 50, 60, 70])
        teor_fosforo['medio'] = fuzz.trapmf(x_teor_fosforo, [60, 70, 90, 100])
        teor_fosforo['pouco_alto'] = fuzz.trapmf(x_teor_fosforo, [90, 100, 110, 120])
        teor_fosforo['alto'] = fuzz.trapmf(x_teor_fosforo, [110, 120, 160, 180])
        teor_fosforo['muito_alto'] = fuzz.trapmf(x_teor_fosforo, [160, 200, 250, 270])
        teor_fosforo['muito_muito_alto'] = fuzz.smf(x_teor_fosforo, 250, 270)


        fosforo_por_ha['muito_baixo'] = fuzz.zmf(x_fosforo_por_ha, 20, 40)
        fosforo_por_ha['baixo'] = fuzz.trapmf(x_fosforo_por_ha, [20, 40, 60, 80])
        fosforo_por_ha['medio'] = fuzz.trapmf(x_fosforo_por_ha, [60, 80, 90, 110])
        fosforo_por_ha['alto'] = fuzz.trapmf(x_fosforo_por_ha, [90, 110, 130, 140])
        fosforo_por_ha['muito_alto'] = fuzz.trapmf(x_fosforo_por_ha, [130, 140, 150, 150])


        # Definindo o sistema de regras
        rules = []

        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))

        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))

        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))

        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))


        # Criar o sistema de controle fuzzy
        fosforo_ctrl = ctrl.ControlSystem(rules)
        fosforo_sim = ctrl.ControlSystemSimulation(fosforo_ctrl)


        # Definir as entradas para a simulação
        fosforo_sim.input['teor_argila'] = argila_entrada  # Exemplo de valor de argila
        fosforo_sim.input['teor_fosforo'] = fosforo_entrada  # Exemplo de valor de fosforo

        # Calcular a saída
        fosforo_sim.compute()

        # Obter e exibir o resultado
        resultado = fosforo_sim.output['fosforo_saida']

        return resultado
