import random
thanos = random.randrange(1, 50)
dif = int(input("1-Fácil(15)\n2-Médio(10)\n3-Difícil(5)\nEscolha a dificuldade: "))
if dif == 1:
    tentativas = 15
elif dif == 2:
    tentativas = 10
else:
    tentativas = 5
    for x in range(0, tentativas):
        escolha = int(input("Qual árvore thanos está(1 a 50): "))
        if thanos < escolha:
                print("Thanos está a esquerda")
        elif thanos > escolha:
                print("Thanos está a direita")
        else:
                print("Você achou o Thanos")
                break