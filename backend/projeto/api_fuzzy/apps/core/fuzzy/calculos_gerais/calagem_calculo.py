

class Calcario:
    def fazCalculo(indice_smp: float, ph_escolha: float, ph_desejado: float) -> float:
        #Verifica se o ph de escolha é maior que o smp, se for, não precisa de adição de calcario
        if(float(indice_smp) >= ph_escolha):
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
    
        magnesio_esperado = 0.2 * ctc 
        diferenca_magnesio = magnesio_esperado - magnesio

        quantidade_calcario_calcitico_necessario = diferenca_magnesio * 2000000 / 2 
        
        #Se a diferença de magnesio for negativa também nao precisa de mais magnesio
        #Se a quantidade de magnesio que contem no calcario calcitico for suficiente
        #para atender a necessidade de magnesio, o tipo de calcario escolhido vai ser o Calcítico
        if quantidade_calcario_calcitico_necessario < calcario_a_aplicar:
            return 'Calcário Calcítico'
        
        calcio_esperado = 0.6 * ctc 
        diferenca_calcio = calcio_esperado - calcio

        quantidade_calcario_dolomitico_necessario = diferenca_calcio * 2000000 / 25

        #Se a diferença de calcio for negativa também nao precisa de mais calcio
        #Se a quantidade de calcio que contem no calcario dolomitico for suficiente
        #para atender a necessidade de calcio, o tipo de calcario escolhido vai ser o Dolomitico
        if quantidade_calcario_dolomitico_necessario < calcario_a_aplicar:
            return 'Calcário Dolomítico'

        #falta só a excessão para mistura dos dois
        return 'Calcário Dolomítico e Calcário Calcítico'
