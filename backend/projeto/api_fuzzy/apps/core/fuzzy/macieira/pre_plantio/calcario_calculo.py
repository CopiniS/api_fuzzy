

class Calcario:
    def fazCalculo(indice_smp: float) -> float:
        if(float(indice_smp) >= 6):
            print('indice_smp maior que 6', indice_smp)
            return 0
        tabela = {
            4.4: 29.0, 
            4.5: 21.0, 
            4.6: 17.3, 
            4.7: 15.1, 
            4.8: 13.3,
            4.9: 11.9, 
            5.0: 10.7, 
            5.1: 9.9, 
            5.2: 9.1, 
            5.3: 8.3,
            5.4: 7.5, 
            5.5: 6.8, 
            5.6: 6.1, 
            5.7: 5.4, 
            5.8: 4.8,
            5.9: 4.2, 
        }
        
        print(tabela.get(indice_smp, 0))
        return tabela.get(indice_smp, 0)

   