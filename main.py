import time
import requests
import json
from joblib import Parallel, delayed

t1 = time.time()
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
parametros = {}
resposta = requests.request("GET", url, params=parametros)

if resposta.status_code != 200:
    erro = f"Não foi possível realizar a consulta. Erro encontrado: {resposta.status_code}, {resposta.text}"
    raise Exception(erro)

objetos = json.loads(resposta.text)
dados = objetos['dados']

print(resposta.status_code, len(dados))

dados_simplificados_deputados = []
# for dado in dados:

def gera_dados_simplificados(dado):

    dados_simplificados_deputados.append({
            'Nome': dado.get('nome'),
            'SiglaPartido': dado.get('siglaPartido')
        }
    )
    return dados_simplificados_deputados

resultado = Parallel(n_jobs=2)(delayed(gera_dados_simplificados)(dado) for dado in dados)

print(resultado)
print(f"Tempo de execução {time.time() - t1}")
# demorou 18 segundos sem paralelismo

#com paralelismo demorou 2 segundos

print(dados_simplificados_deputados)



