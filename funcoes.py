import random

def rolar_dados(n):

    resposta =[]
    
    i = 0

    while i < n:
        resposta.append(random.randint(1,6))
        i +=1
    return resposta    

def guardar_dado(dados_rolados, dados_guardados, indice):

    dado = dados_rolados.pop(indice)
    
    dados_guardados.append(dado)
    return [dados_rolados, dados_guardados]   

    def remover_dado(dados_rolados, dados_guardados, n):
        resposta = []
        dados_rolados.append(dados_guardados[n])

        return dados_rolados