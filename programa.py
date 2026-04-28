

from funcoes import *

def jogo():

    cartela = {
        'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
        'regra_avancada': {
            'sem_combinacao':-1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }
    }

    rodada = 0

    while rodada < 12:

        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerrolagens = 0
        jogada_feita = False

        while not jogada_feita:

            print("Dados rolados:", dados_rolados)
            print("Dados guardados:", dados_guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input())

                if indice < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input())

                if indice < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

            elif opcao == "3":
                if rerrolagens < 2:
                    dados_rolados = rolar_dados(len(dados_rolados))
                    rerrolagens += 1
                else:
                    print("Você já usou todas as rerrolagens.")

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":

                valido = False

                while not valido:
                    print("Digite a combinação desejada:")
                    categoria = input()

                    if categoria.isdigit():
                        categoria_int = int(categoria)

                        if categoria_int not in cartela['regra_simples']:
                            print("Combinação inválida. Tente novamente.")
                        elif cartela['regra_simples'][categoria_int] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            valido = True

                    else:
                        if categoria not in cartela['regra_avancada']:
                            print("Combinação inválida. Tente novamente.")
                        elif cartela['regra_avancada'][categoria] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            valido = True

                dados = dados_rolados + dados_guardados
                cartela = faz_jogada(dados, categoria, cartela)

                jogada_feita = True

            else:
                print("Opção inválida. Tente novamente.")

        rodada += 1

    total = 0

    for valor in cartela['regra_simples'].values():
        total += valor

    for valor in cartela['regra_avancada'].values():
        total += valor

    soma_simples = 0
    for valor in cartela['regra_simples'].values():
        soma_simples += valor

    if soma_simples >= 63:
        total += 35

    imprime_cartela(cartela)
    print(f"Pontuação total: {total}")


    jogo()