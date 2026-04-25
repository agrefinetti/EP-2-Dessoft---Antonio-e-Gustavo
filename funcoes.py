import random

def rolar_dados(n):

    resposta =[]
    
    i = 0

    while i < n:
        resposta.append(random.randint(1,6))
        i +=1
    return resposta    