def is_blackjack(mao):
    total = sum(mao)
    if total == 21:
        return True
    return None
def vez_do_dealer():
    mao = []
    while sum(mao) < 18:
        mao.append(pega_carta())
        mao = eval_ace(mao)
    return mao
def compara_entre(jogador, dealer):
    total_jogador = sum(jogador)
    total_dealer = sum(dealer)
    jogador_bust = is_bust(jogador)
    dealer_bust = is_bust(dealer)
    player_blackjack = is_blackjack(jogador)
    dealer_blackjack = is_blackjack(dealer)
    pontos_do_jogador = 0
    pontos_do_dealer = 0
    if jogador_bust:
        if (not dealer_blackjack and
                total_dealer < 21):
            pontos_do_dealer += 1
    if dealer_bust:
        if (not player_blackjack and
                total_jogador < 21):
            pontos_do_jogador += 1
    if (jogador_bust and
            dealer_bust):
        if (total_jogador > total_dealer):
            pontos_do_jogador += 1
        elif (total_dealer > total_jogador):
            pontos_do_dealer += 1
        else:
            pontos_do_jogador == pontos_do_dealer
    if player_blackjack:
        pontos_do_jogador += 1
    if dealer_blackjack:
        pontos_do_dealer += 1
    if (player_blackjack and
            dealer_blackjack):
        pontos_do_jogador == pontos_do_dealer
    if (total_jogador < 21 and
            total_dealer < 21):
        if (total_jogador > total_dealer):
            pontos_do_jogador += 1
        elif (total_dealer > total_jogador):
            pontos_do_dealer += 1
        else:
            pontos_do_jogador == pontos_do_dealer
    return pontos_do_jogador, pontos_do_dealer
def resultado_do_jogo(mao_do_jogador, mao_do_dealer):
    print("\nTemos o resultado: ")
    print("Jogador tem: {0} total = {1}".format(
        mao_do_jogador, sum(mao_do_jogador)))    
    print("Dealer tem: {0} total = {1}".format(
        mao_do_dealer, sum(mao_do_dealer)))
    return None
def resultado_final(jogador_venceu, dealer_venceu, jogo):
    print("\nO final, depois de {} jogos:".format(jogo))   
    print("jogador: {} | dealer: {}".format(
        jogador_venceu, dealer_venceu))
    return None
if __name__ == "__main__": main()
   
