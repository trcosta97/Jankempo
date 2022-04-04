import random

# 0 = PEDRA | 1 = TESOURA | 2 = PAPEL

def comeco():
    print("***********************")
    print("**PEDRA PAPEL TESOURA**")
    print("***********************" "\n")

def sorteiaNumero():
    return random.randint(0,2)

def chute():
    return int(input("Digite 1 para Pedra, 2 para Papel ou 3 para Tesoura " "\n"))

def jogar():
    comeco()
    maquina = sorteiaNumero()
    jogador = chute()

    if maquina == 0:
        print("O computador escolheu pedra!")
        if jogador == 1:
            print("Empatou!")
        elif jogador == 2:
            print("Você ganhou!")
        elif jogador == 3:
            print("Você perdeu!")
    elif maquina == 1:
        print("O computador escolheu tesoura!")
        if jogador == 1:
            print("Você perdeu!")
        elif jogador == 2:
            print("Empatou!")
        elif jogador == 3:
            print("Você ganhou!")
    elif maquina == 2:
        print("O computador escolheu papel!")
        if jogador == 1:
            print("Você ganhou!")
        elif jogador == 2:
            print("Você perdeu!")
        elif jogador == 3:
            print("Empatou!")

jogar()




