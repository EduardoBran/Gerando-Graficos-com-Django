from random import randint

from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    

class DadosJSONView(BaseLineChartView):
    
    # retorna 12 labels para a representação do x
    def get_labels(self):
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        return labels
    
    # retorna os nomes dos datasets (serão cursos do Geek até o momento)
    def get_providers(self):
        datasets = [
            "Programação para Leigos",
            "Algoritmos e Lógica de Programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"
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
        for linha in range(6):
            for coluna in range(12):
                dado = [
                    randint(1, 200), # jan
                    randint(1, 200), # fev
                    randint(1, 200), # mar
                    randint(1, 200), # abr
                    randint(1, 200), # mai
                    randint(1, 200), # jun
                    randint(1, 200), # jul
                    randint(1, 200), # ago
                    randint(1, 200), # set
                    randint(1, 200), # out
                    randint(1, 200), # nov
                    randint(1, 200)  # dez
                    
                    # 20, # jan
                    # 10, # fev
                    # 10, # mar
                    # 10, # abr
                    # 10, # mai
                    # 50, # jun
                    # 40, # jul
                    # 10, # ago
                    # 10, # set
                    # 10, # out
                    # 10, # nov
                    # 10  # dez
                ]
            dados.append(dado)
        return dados
    


# os métodos da class class DadosJSONView como
# def get_labels , def get_providers são próprios do BaseLineChartView