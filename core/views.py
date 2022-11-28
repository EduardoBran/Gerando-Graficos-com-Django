from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    

class DadosJSONView(BaseLineChartView):
    
    # retorna 12 labels para a representação do x
    def get_labels(self):
        labels = [
            "2022",
            "2021",
            "2020",
            "2019",
            "2018",
        ]
        return labels
    
    # retorna os nomes dos datasets (serão cursos do Geek até o momento)
    def get_providers(self):
        datasets = [
            "L. Messi",
            "Neymar Jr.",
            "K. Mbappé",
            "C. Ronaldo",
            "R. Lewandowski",
            "K. Benzema",
            "Gabigol"
        ]
        return datasets
    
    # funcao que vai gerar e retornar os dados
    # irá retornar 6 datasets para plotar o gráfico (6 = qtd de cursos)
    # Cada linha representa um dataset
    # Cada coluna representa um label
    # a qtd de dados precisa ser igual aos datasets/labels
    # 12 labels, então 12 colunas | 6 datasets, entao 6 linhas
    def get_data(self):
        dados = []
        for linha in range(7):
            for coluna in range(4): # Messi
                dado1 = [
                    12, # 2022
                    11, # 2021
                    38, # 2020
                    31, # 2019
                    51, # 2018
                ]
        dados.append(dado1)
        
        for linha in range(7):
            for coluna in range(4): # Ney
                dado2 = [
                    15, # 2022
                    13, # 2021
                    17, # 2020
                    19, # 2019
                    23, # 2018
                ]        
        dados.append(dado2)
        
        for linha in range(7):
            for coluna in range(4): # Mbappe
                dado3 = [
                    19, # 2022
                    39, # 2021
                    42, # 2020
                    30, # 2019
                    39, # 2018
                ]        
        dados.append(dado3)
        
        for linha in range(7):
            for coluna in range(4): # C. ronaldo
                dado4 = [
                    3, # 2022
                    24, # 2021
                    36, # 2020
                    37, # 2019
                    28, # 2018
                ]        
        dados.append(dado4)
        
        for linha in range(7):
            for coluna in range(4): # Lewandowski
                dado5 = [
                    18, # 2022
                    50, # 2021
                    48, # 2020
                    55, # 2019
                    40, # 2018
                ]        
        dados.append(dado5)
        
        for linha in range(7):
            for coluna in range(4): # Benzema
                dado6 = [
                    6, # 2022
                    44, # 2021
                    30, # 2020
                    27, # 2019
                    30, # 2018
                ]        
        dados.append(dado6)
        
        for linha in range(7):
            for coluna in range(4): # Gabigol
                dado7 = [
                    29, # 2022
                    34, # 2021
                    27, # 2020
                    43, # 2019
                    27, # 2018
                ]        
        dados.append(dado7)
        
        return dados


# os métodos da class class DadosJSONView como
# def get_labels , def get_providers são próprios do BaseLineChartView