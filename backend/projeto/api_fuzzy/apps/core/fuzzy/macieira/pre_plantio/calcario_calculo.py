

class Calcario:
    def fazCalculo(indice_smp: str) -> float:
        if(float(indice_smp) >= 6):
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
        
        # Retorna a quantidade exata ou 0 se o índice não estiver na tabela
        return tabela.get(indice_smp, 0)

   