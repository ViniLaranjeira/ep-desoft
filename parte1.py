from random import randrange
def main():
    print_intro()
    jogador_venceu, dealer_venceu, jogo = jogar_varias_vezes()
    resultado_final(jogador_venceu, dealer_venceu, jogo)
def print_intro():
    print("Blackjack (vinte um) eh um jogo de cassino jpgado com cartas.")
    print("o objetivo do jogo eh ficar com cartas que somam um total o mais proximo possivel de 21")
    print("sem passar do limite (a mao que ficar com mais de 21 perde). Todas as cartas com cara (reis, damas e valetes) valem 10,")
    print("as conta como 1 ou 11, todas as outras cartas valem seu valor numerico.")
    print("primeiramente, sua vez:")
    return None
def jogar_varias_vezes():
    jogador_venceu = 0
    dealer_venceu = 0
    jogo = 0
    jogar_novamente = "sim"
    while (jogar_novamente[0] == "s" or jogar_novamente[0] == "S"):
        mao_do_jogador = vez_do_jogador()
        mao_do_dealer = vez_do_dealer()
        pontos_do_jogador, pontos_do_dealer = compara_entre(mao_do_jogador, mao_do_dealer)
        resultado_do_jogo(mao_do_jogador, mao_do_dealer)
        if (pontos_do_jogador > pontos_do_dealer):
            print("\nPlayer Veeenceu!")
            jogador_venceu += 1
        elif (pontos_do_dealer > pontos_do_jogador):
            print("\nDealer Veeenceu!")
            dealer_venceu += 1
        else:
            print("\nEsse jogo eh um empate!")
            jogador_venceu == dealer_venceu
        jogo += 1
        jogar_novamente = input("\nQuer jogar denovo (S ou N)?")      
    return jogador_venceu, dealer_venceu, jogo   
def vez_do_jogador():
    mao = []
    ans = "hit"
    mao.append(pega_carta())
    while (ans[0] == "h" or ans[0] == "H"):
        mao.append(pega_carta())
        mao = eval_ace(mao)
        print("\nSua mao: {0} total = {1}".format(mao, sum(mao)))
        if (is_bust(mao) or
            is_blackjack(mao)):
            break
        ans = input("Voce vai dar Hit ou Stand (H or S)?")
    return mao
def pega_carta():
    embaralha_cartas = randrange(2, 11 + 1)
    return embaralha_cartas
def eval_ace(mao):
    total = sum(mao)
    for ace in mao:
        if (ace == 11 and total > 21):
            posicao_as = mao.index(11)
            mao[posicao_as] = 1
    return mao
def is_bust(mao):
    total = sum(mao)
    if total > 21:
        return True
    return None