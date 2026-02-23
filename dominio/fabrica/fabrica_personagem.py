from dominio.personagens.guerreiro import Guerreiro
from dominio.personagens.arqueiro import Arqueiro

from dominio.enums.classe_personagem import ClassePersonagem
from dominio.enums.tipo_habilidade import TipoHabilidade

from dominio.fabrica.fabrica_habilidade import FabricaHabilidade


class FabricaPersonagem:

    @staticmethod
    def criar(classe: ClassePersonagem, nome: str):

        if classe == ClassePersonagem.GUERREIRO:
            personagem = Guerreiro(nome)

        elif classe == ClassePersonagem.ARQUEIRO:
            personagem = Arqueiro(nome)

        else:
            raise ValueError("Classe inválida")

        # 🔥 Build inicial padrão do jogo
        FabricaPersonagem._aplicar_build_inicial(personagem)

        return personagem

    @staticmethod
    def _aplicar_build_inicial(personagem):

        # Todo mundo recebe ataque básico
        habilidade_basica = FabricaHabilidade.criar(
            personagem,
            TipoHabilidade.ATAQUE_BASICO
        )
        personagem.adicionar_habilidade(habilidade_basica)

        # Especial depende da classe
        if personagem.classe == ClassePersonagem.GUERREIRO:
            especial = FabricaHabilidade.criar(
                personagem,
                TipoHabilidade.GOLPE_PESADO
            )

        elif personagem.classe == ClassePersonagem.ARQUEIRO:
            especial = FabricaHabilidade.criar(
                personagem,
                TipoHabilidade.DISPARO_TRIPLO
            )

        personagem.adicionar_habilidade(especial)