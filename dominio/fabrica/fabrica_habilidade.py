from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.classe_personagem import ClassePersonagem

from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.guerreiro import GolpePesado
from dominio.habilidades.arqueiro import DisparoTriplo


class FabricaHabilidade:

    # 🔥 Regras centrais do jogo
    HABILIDADES_PERMITIDAS = {
        ClassePersonagem.GUERREIRO: {
            TipoHabilidade.ATAQUE_BASICO,
            TipoHabilidade.GOLPE_PESADO,
        },
        ClassePersonagem.ARQUEIRO: {
            TipoHabilidade.ATAQUE_BASICO,
            TipoHabilidade.DISPARO_TRIPLO,
        },
    }

    @staticmethod
    def criar(personagem, tipo: TipoHabilidade):

        classe = personagem.classe

        if tipo not in FabricaHabilidade.HABILIDADES_PERMITIDAS[classe]:
            raise ValueError(
                f"{tipo.name} não permitido para {classe.value}"
            )

        if tipo == TipoHabilidade.ATAQUE_BASICO:
            return AtaqueBasico(personagem)

        if tipo == TipoHabilidade.GOLPE_PESADO:
            return GolpePesado(personagem)

        if tipo == TipoHabilidade.DISPARO_TRIPLO:
            return DisparoTriplo(personagem)

        raise ValueError("Habilidade não implementada")