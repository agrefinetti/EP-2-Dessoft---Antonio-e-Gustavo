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

def remover_dado(dados_rolados, dados_no_estoque, indice):
    valor = dados_no_estoque[indice]
    dados_rolados.append(valor)

    nova_lista = []
    i = 0

    while i < len(dados_no_estoque):
        if i != indice:
            nova_lista.append(dados_no_estoque[i])
        i += 1

    return [dados_rolados, nova_lista]