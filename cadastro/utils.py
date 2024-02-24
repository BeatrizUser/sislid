import csv
from cadastro.models import *

def exportar_dados_csv(nome_arquivo):
    # Query para obter os dados que você deseja exportar
    dados = Pessoa.objects.all()

    # Cabeçalhos do CSV (opcional, mas útil para identificar colunas)
    cabecalhos = ['coluna1', 'coluna2', 'coluna3']  # Substitua pelos nomes das suas colunas

    # Abra um arquivo CSV em modo de escrita
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        # Crie um escritor CSV
        escritor_csv = csv.writer(arquivo_csv)
        
        # Escreva o cabeçalho no arquivo CSV
        escritor_csv.writerow(cabecalhos)
        
        # Escreva os dados no arquivo CSV
        for dado in dados:
            # Substitua 'coluna1', 'coluna2', 'coluna3' pelos nomes dos atributos do seu modelo
            linha = [dado.coluna1, dado.coluna2, dado.coluna3]
            escritor_csv.writerow(linha)
