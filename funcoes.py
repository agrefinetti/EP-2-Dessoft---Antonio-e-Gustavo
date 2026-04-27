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

def calcula_pontos_regra_simples(lista_numeros):

    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    
    for numero in lista_numeros:
        dic[numero] += numero
            
    return dic

def calcula_pontos_soma(lista_inteiros):
    resposta = 0
    for i in range(len(lista_inteiros)):
        resposta += lista_inteiros[i]
    return resposta

def calcula_pontos_sequencia_baixa(lista_inteiros):
    if (1 in lista_inteiros and 2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros):
        return 15
    if (2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros and 5 in lista_inteiros):
        return 15
    if (3 in lista_inteiros and 4 in lista_inteiros and 5 in lista_inteiros and 6 in lista_inteiros):
        return 15   
    return 0   
def calcula_pontos_sequencia_alta(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista):
        return 30
    if (2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 30
    return 0