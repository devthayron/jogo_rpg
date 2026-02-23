from sistema.acoes import Acao
from dominio.enums.tipo_habilidade import TipoHabilidade


def iniciar_terminal(batalha):
    while not batalha.acabou():
        _exibir_status(batalha)
        acao, tipo = _escolher_acao(batalha.jogador)
        resultado_jogador, resultado_inimigo = batalha.executar_turno(
            acao_jogador=acao,
            tipo_habilidade=tipo
        )
        _exibir_resultado("Jogador", resultado_jogador)
        _exibir_resultado("Inimigo", resultado_inimigo)

    _exibir_fim(batalha)


def _exibir_status(batalha):
    status = batalha.status()
    print("\n========================")
    print(f"Turno: {status['turno']}")
    print(status["jogador"])
    print(status["inimigo"])
    print("========================\n")


def _escolher_acao(personagem):
    print("Escolha sua ação:")
    print("1 - Usar habilidade")
    print("2 - Passar turno")

    while True:
        try:
            escolha = int(input(">> "))
            if escolha == 1:
                # força o terminal a atualizar a lista de habilidades
                habilidades = personagem.listar_habilidades()
                if not habilidades:
                    print("Nenhuma habilidade disponível.")
                    continue
                return Acao.USAR_HABILIDADE, _escolher_habilidade(personagem)
            if escolha == 2:
                return Acao.PASSAR_TURNO, None
        except ValueError:
            pass
        print("Escolha inválida.")


def _escolher_habilidade(personagem):
    print("\nEscolha sua habilidade:")
    habilidades = personagem.listar_habilidades()

    # 🔥 exibe habilidades com índice
    for idx, nome in enumerate(habilidades, 1):
        print(f"{idx} - {nome}")

    while True:
        try:
            escolha = int(input(">> ")) - 1
            nome_escolhido = habilidades[escolha]
            # converte string para enum
            return TipoHabilidade[nome_escolhido]
        except (ValueError, IndexError, KeyError):
            print("Escolha inválida.")


def _exibir_resultado(nome, resultado):
    if resultado is None:
        print(f"{nome} passou o turno.")
        return

    if resultado.executado:
        print(
            f"{nome} usou {resultado.tipo.name} "
            f"e causou {resultado.dano} de dano "
            f"(energia gasta: {resultado.energia_gasta})"
        )
    else:
        print(f"{nome} falhou: {resultado.motivo_falha.name}")


def _exibir_fim(batalha):
    print("\n===== FIM DA BATALHA =====")
    if batalha.jogador.esta_vivo():
        print("Vitória.")
    else:
        print("Derrota.")