from dominio.enums.classe_personagem import ClassePersonagem
from dominio.fabrica.fabrica_personagem import FabricaPersonagem

from sistema.batalha import Batalha
from interface.terminal.terminal import iniciar_terminal


def main():

    jogador = FabricaPersonagem.criar(
        ClassePersonagem.GUERREIRO,
        "Heroi"
    )

    inimigo = FabricaPersonagem.criar(
        ClassePersonagem.ARQUEIRO,
        "Goblin"
    )

    batalha = Batalha(jogador, inimigo)

    iniciar_terminal(batalha)


if __name__ == "__main__":
    main()