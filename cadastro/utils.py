import requests

def preencher_local_de_votacao(zona, secao):
    try:
        url = f"https://apps.tre-rj.jus.br/api-dados-abertos/locaisvotacao/municipio/S%C3%A3o%20Gon%C3%A7alo"
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        locais_votacao = response.json()
        
        for local in locais_votacao:
            secoes = local["secoes"].split(",")  # Divide as seções em uma lista de strings
            if str(secao) in secoes and int(local["numZona"]) == zona:
                return local["local"], local["endereco"], local["bairro"], local["cep"]
    except Exception as e:
        print(f"Erro ao buscar locais de votação: {e}")

    return None, None, None, None
