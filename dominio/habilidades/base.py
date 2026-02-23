from abc import ABC, abstractmethod

from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.motivo_falha import MotivoFalha
from dominio.personagens.personagem import Personagem


class Habilidade(ABC):

    def __init__(self, personagem: Personagem):
        self.personagem = personagem
        self.tipo = None
        self.custo = 0

    def validar(self, alvo: Personagem):
        if not isinstance(alvo, Personagem):
            return False, MotivoFalha.ALVO_INVALIDO

        if not self.personagem.esta_vivo():
            return False, MotivoFalha.ATACANTE_MORTO

        if not alvo.esta_vivo():
            return False, MotivoFalha.ALVO_MORTO

        if self.personagem.energia < self.custo:
            return False, MotivoFalha.SEM_ENERGIA

        return True, None

    def executar(self, alvo: Personagem):
        valido, motivo = self.validar(alvo)

        if not valido:
            return ResultadoAtaque(
                executado=False,
                motivo_falha=motivo,
                tipo=self.tipo
            )

        return self._executar(alvo)

    @abstractmethod
    def _executar(self, alvo: Personagem) -> ResultadoAtaque:
        pass


# ---------------- ATAQUE BASICO ----------------

class AtaqueBasico(Habilidade):

    def __init__(self, personagem: Personagem):
        super().__init__(personagem)
        self.tipo = TipoHabilidade.ATAQUE_BASICO
        self.custo = 20

    def _executar(self, alvo: Personagem):
        self.personagem.gastar_energia(self.custo)

        dano_final = self.personagem.dano
        alvo.receber_dano(dano_final)

        return ResultadoAtaque(
            executado=True,
            dano=dano_final,
            energia_gasta=self.custo,
            tipo=self.tipo
        )