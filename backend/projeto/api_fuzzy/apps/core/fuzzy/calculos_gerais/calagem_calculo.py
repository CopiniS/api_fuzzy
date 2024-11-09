

from typing import Dict, Tuple


class Calcario:
    def defineCalagem(  
    area_plantada: float,
    indice_smp: float, 
    ph_escolha: float, 
    ph_desejado: float,
    ca_inicial: float, 
    mg_inicial: float, 
    sat_ca_min: float,
    sat_ca_max: float,
    sat_mg_min: float, 
    sat_mg_max: float,
    ctc: float
    ) -> Dict[str, Tuple[float, float]]:
        
        calcario_por_ha = int(Calcario.fazCalculo(indice_smp, ph_escolha, ph_desejado) * 1000)
        melhor_calcitico, melhor_dolomitico, melhor_sat_ca_final, melhor_sat_mg_final, erro_total_minimo = Calcario.escolheTipoMisto(
            calcario_por_ha, 
            ca_inicial, 
            mg_inicial, 
            sat_ca_min,
            sat_ca_max,
            sat_mg_min, 
            sat_mg_max,
            ctc
        )

        print('melhor_sat_ca_final: ', melhor_sat_ca_final)
        print('melhor_sat_mg_final: ', melhor_sat_mg_final)
        print('erro_total_minimo: ', erro_total_minimo) 
        print('melhor_calcitico: ', melhor_calcitico)
        print('melhor_dolomitico: ', melhor_dolomitico)

        
        total = calcario_por_ha * area_plantada
        if melhor_dolomitico == 0: #Esse é o padrão. Caso mg e ca ja estejam satisfeitos, ou seja se melhor calcitico for 0 e melhor dolomitico for 0
            return {
                'Calcario Calcítico': (calcario_por_ha, total),
                'Calcario Dolomitico': (0, 0)
            }

        if melhor_calcitico == 0:
            return {
                'Calcario Calcítico': (0, 0),
                'Calcario Dolomitico': (calcario_por_ha, total)
            }
        
        total_calcitico = melhor_calcitico * area_plantada
        total_domotico = melhor_dolomitico * area_plantada
        return {
            'Calcario Calcítico': (melhor_calcitico, total_calcitico),
            'Calcario Dolomitico': (melhor_dolomitico, total_domotico)
        }
        
    def fazCalculo(indice_smp: float, ph_escolha: float, ph_desejado: float) -> float:
        #Verifica se o ph de escolha é maior que o smp, se for, não precisa de adição de calcario
        if(indice_smp >= ph_escolha):
            print('indice_smp: ', indice_smp)
            print('ph_escolha: ', ph_escolha)
            return 0
        match ph_desejado:
            case 5.5:
                tab55 = {
                    4.4: 15.0, 4.5: 12.5, 4.6: 10.9, 4.7: 9.6, 4.8: 8.5,
                    4.9: 7.7, 5.0: 6.6, 5.1: 6.0, 5.2: 5.3, 5.3: 4.8,
                    5.4: 4.2, 5.5: 3.7, 5.6: 3.2, 5.7: 2.8, 5.8: 2.3,
                    5.9: 2.0, 6.0: 1.6, 6.1: 1.3, 6.2: 1.0, 6.3: 0.8,
                    6.4: 0.6, 6.5: 0.4, 6.6: 0.2, 6.7: 0, 6.8: 0,
                    6.9: 0, 7.0: 0, 7.1: 0
                }

                return tab55.get(indice_smp, 0)

            case 6:
                tab60 = {
                    4.4: 21.0, 4.5: 17.3, 4.6: 15.1, 4.7: 13.3, 4.8: 11.9,
                    4.9: 10.7, 5.0: 9.9, 5.1: 9.1, 5.2: 8.3, 5.3: 7.5,
                    5.4: 6.8, 5.5: 6.1, 5.6: 5.4, 5.7: 4.8, 5.8: 4.2,
                    5.9: 3.7, 6.0: 3.2, 6.1: 2.7, 6.2: 2.2, 6.3: 1.8,
                    6.4: 1.4, 6.5: 1.1, 6.6: 0.8, 6.7: 0.5, 6.8: 0.3,
                    6.9: 0.2, 7.0: 0, 7.1: 0
                }
                return tab60.get(indice_smp, 0)

            case 6.5:
                tab65 = {
                    4.4: 29.0, 4.5: 24.0, 4.6: 20.0, 4.7: 17.5, 4.8: 15.7,
                    4.9: 14.2, 5.0: 13.3, 5.1: 12.3, 5.2: 11.3, 5.3: 10.4,
                    5.4: 9.5, 5.5: 8.6, 5.6: 7.8, 5.7: 7.0, 5.8: 6.3,
                    5.9: 5.6, 6.0: 4.9, 6.1: 4.3, 6.2: 3.7, 6.3: 3.1,
                    6.4: 2.6, 6.5: 2.1, 6.6: 1.6, 6.7: 1.2, 6.8: 0.8,
                    6.9: 0.5, 7.0: 0.2, 7.1: 0
                }

                return tab65.get(indice_smp, 0)

            case _:
                raise ValueError("ph_desejado inválido. O valor do ph desejado deve ser 5.5 ou 6 ou 6.5")
            
    def escolheTipo(calcio: float, magnesio: float, ctc: float, calcario_a_aplicar: float) -> str:
        saturacao_c = 100 *calcio / ctc
        saturacao_m = 100 * magnesio / ctc
    

        #MAGNESIO EM CALCÍTICO
        magnesio_esperado = 0.2 * ctc 
        diferenca_magnesio = magnesio_esperado - magnesio
        constante_magnesio_em_calcitico = 2000000 / 2 # valor retirado de considerações_calcario.txt

        quantidade_calcario_calcitico_necessario = diferenca_magnesio * constante_magnesio_em_calcitico 
        
        #Se a diferença de magnesio for negativa também nao precisa de mais magnesio
        #Se a quantidade de magnesio que contem no calcario calcitico for suficiente
        #para atender a necessidade de magnesio, o tipo de calcario escolhido vai ser o Calcítico
        if quantidade_calcario_calcitico_necessario < calcario_a_aplicar:
            return 'Calcário Calcítico'
        

        #CALCIO EM DOLOMÍTICO
        calcio_esperado = 0.6 * ctc # quantidade de calcio que deve ser adicionado para chegar em 60% de saturação
        diferenca_calcio = calcio_esperado - calcio #diferença de calcio esperado e o calcio que está no solo
        constante_calcio_em_dolomitico = 2000000 / 25 # valor retirado de considerações_calcario.txt. 2.000.000 é o volume de solo em dm³ e 25 é a qunatidade de calcio em cmolc/kg de calcário dolomítico

        quantidade_calcario_dolomitico_necessario = diferenca_calcio * constante_calcio_em_dolomitico

        #Se a quantidade de calcio que contem no calcario dolomitico for suficiente
        #para atender a necessidade de calcio, o tipo de calcario escolhido vai ser o Dolomitico
        #Se a diferença de calcio for negativa também nao precisa de mais calcio
        if quantidade_calcario_dolomitico_necessario < calcario_a_aplicar:
            return 'Calcário Dolomítico'
        

        #CALCIO EM AMBOS e MAGNESIO EM AMBOS



        grau_de_saturacao_c = saturacao_c / 60 #Quanto mais perto de 1, mais correto
        grau_de_saturacao_m = saturacao_m / 20 #Quanto mais perto de 1, mais correto


        return 'Calcário Dolomítico e Calcário Calcítico'

    def escolheTipoMisto(
        calcario_por_ha: int, 
        ca_inicial: float, #quantidade que vem do laudo em cmolc/dm³
        mg_inicial: float, #quantidade que vem do laudo em cmolc/dm³
        sat_ca_min: float,
        sat_ca_max: float,
        sat_mg_min: float, 
        sat_mg_max: float,
        ctc: float
    ) -> Tuple[float, float, float, float, float]:
        #CONSTANTES
        constante_profundidade_metros = 0.2  # Profundidade do solo em metros
        constante_ca_calcitico = 35  # quantidade de calcio em cmolc por kg de carcario calcitico
        constante_ca_dolomitico = 25  # quantidade de calcio em cmolc por kg de carcario dolomitico
        constante_mg_calcitico = 2  # quantidade de mg em cmolc por kg de carcario calcitico
        constante_mg_dolomitico = 20  # quantidade de mg em cmolc por kg de carcario dolomitico
        constante_volume_por_ha = 10.000 * constante_profundidade_metros * 1000 # volume do solo em dm³
        sat_ca_inicial = 100 * ca_inicial / ctc  #saturaçao de calcio inicial
        sat_mg_inicial = 100 * mg_inicial / ctc   #saturaçao de mg inicial

        print('calcario_por_ha: ', calcario_por_ha)
        print('sat_ca_inicial: ', sat_ca_inicial)
        print('sat_mg_inicial: ', sat_mg_inicial)

        # Calcula os incrementos de ca e mg para cada divisão de calcitico e dolomitico
        increment_ca_calcitico = constante_ca_calcitico / constante_volume_por_ha   # a cada 1 kg aumentado de calcario calcitico, aumenta-se esse valor de ca  em cmolc/dm³
        increment_ca_dolomitico = constante_ca_dolomitico / constante_volume_por_ha # a cada 1 kg aumentado de calcario dolomitico, aumenta-se esse valor de ca em cmolc/dm³
        increment_mg_calcitico = constante_mg_calcitico / constante_volume_por_ha   # a cada 1 kg aumentado de calcario calcitico, aumenta-se esse valor de mg em cmolc/dm³
        increment_mg_dolomitico = constante_mg_dolomitico / constante_volume_por_ha # a cada 1 kg aumentado de calcario dolomitico, aumenta-se esse valor de mg em cmolc/dm³

        print('increment_ca_calcitico: ', increment_ca_calcitico)
        print('increment_ca_dolomitico: ', increment_ca_dolomitico)
        print('increment_mg_calcitico: ', increment_mg_calcitico)
        print('increment_mg_dolomitico: ', increment_mg_dolomitico)


        
        melhor_calcitico, melhor_dolomitico = 0, 0  # Divisão inicial
        melhor_sat_ca_final, melhor_sat_mg_final = sat_ca_inicial, sat_mg_inicial  # Começa com os valores iniciais das saturacoes
        erro_total_minimo = float('inf')  # Inicializa o erro com um número muito grande

        # Loop através dos valores possíveis de calcitico, de 0 até calcario_por_ha, e calcula dolomitico de acordo
        for calcitico in range(0, calcario_por_ha + 1):
            dolomitico = calcario_por_ha - calcitico
            
            # Calcula ca e mg após aplicar os incrementos com a divisão atual de calcitico e dolomitico
            sat_ca_final = sat_ca_inicial + calcitico * increment_ca_calcitico + dolomitico * increment_ca_dolomitico
            sat_mg_final = sat_mg_inicial + calcitico * increment_mg_calcitico + dolomitico * increment_mg_dolomitico

            # Calcula os erros se ca ou mg estiverem fora de seus intervalos
            erro_ca = max(0, sat_ca_min - sat_ca_final, sat_ca_final - sat_ca_max)  # Penalidade se ca estiver fora do intervalo [sat_ca_min, sat_ca_max]
            erro_mg = max(0, sat_mg_min - sat_mg_final, sat_mg_final - sat_mg_max)  # Penalidade se mg estiver fora do intervalo [sat_mg_min, sat_mg_max]
            erro_total = erro_ca + erro_mg  # Soma dos erros

            # Verifica se a divisão atual é melhor que a anterior, minimizando o erro total
            if erro_total < erro_total_minimo:
                melhor_calcitico, melhor_dolomitico = calcitico, dolomitico
                melhor_sat_ca_final, melhor_sat_mg_final = sat_ca_final, sat_mg_final
                erro_total_minimo = erro_total

        return melhor_calcitico, melhor_dolomitico, melhor_sat_ca_final, melhor_sat_mg_final, erro_total_minimo