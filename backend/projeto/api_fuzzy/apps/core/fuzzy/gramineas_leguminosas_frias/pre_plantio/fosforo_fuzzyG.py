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

        fosforo_por_ha['muito_baixo'] = fuzz.zmf(x_fosforo_por_ha, 5, 10)
        fosforo_por_ha['baixo'] = fuzz.trapmf(x_fosforo_por_ha, [30, 50, 70, 90])
        fosforo_por_ha['medio'] = fuzz.trapmf(x_fosforo_por_ha, [70, 90, 110, 130])
        fosforo_por_ha['alto'] = fuzz.trapmf(x_fosforo_por_ha, [110, 130, 150, 170])
        fosforo_por_ha['muito_alto'] = fuzz.smf(x_fosforo_por_ha, 160, 170)

        # Definindo o sistema de regras
        rules = []

        # Faixa 1 - Argila muito alta
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['medio'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_1'] & teor_fosforo['muito_muito_alto'], fosforo_por_ha['muito_baixo']))

        # Faixa 2 - Argila alta
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_2'] & teor_fosforo['muito_muito_alto'], fosforo_por_ha['muito_baixo']))

        # Faixa 3 - Argila média
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_3'] & teor_fosforo['muito_muito_alto'], fosforo_por_ha['muito_baixo']))

        # Faixa 4 - Argila baixa
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['muito_baixo'], fosforo_por_ha['muito_alto']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['baixo'], fosforo_por_ha['alto']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['pouco_baixo'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['medio'], fosforo_por_ha['medio']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['pouco_alto'], fosforo_por_ha['baixo']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['muito_alto'], fosforo_por_ha['muito_baixo']))
        rules.append(ctrl.Rule(argila['faixa_4'] & teor_fosforo['muito_muito_alto'], fosforo_por_ha['muito_baixo']))


        # Criar o sistema de controle fuzzy
        fosforo_ctrl = ctrl.ControlSystem(rules)
        fosforo_sim = ctrl.ControlSystemSimulation(fosforo_ctrl)


        # Definir as entradas para a simulação
        fosforo_sim.input['teor_argila'] = float(argila_entrada)  # Exemplo de valor de argila
        fosforo_sim.input['teor_fosforo'] = float(fosforo_entrada)  # Exemplo de valor de fosforo

        # Calcular a saída
        fosforo_sim.compute()

        # Obter e exibir o resultado
        resultado = fosforo_sim.output['fosforo_saida']

        return resultado