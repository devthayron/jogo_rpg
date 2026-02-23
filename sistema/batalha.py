from dominio.personagens.personagem import Personagem
from sistema.executor import Executor
from sistema.acoes import Acao
import random

class Batalha:
    def __init__(self, jogador: Personagem, inimigo: Personagem):
        self.jogador = jogador
        self.inimigo = inimigo
        self.turno = 1

    def acabou(self):
        return not (
            self.jogador.esta_vivo() and
            self.inimigo.esta_vivo()
        )

    def status(self):
        return {
            "jogador": str(self.jogador),
            "inimigo": str(self.inimigo),
            "turno": self.turno
        }

    def executar_turno(self, acao_jogador, tipo_habilidade=None):
        # ---------------- Jogador ----------------
        resultado_jogador = Executor.executar(
            atacante=self.jogador,
            alvo=self.inimigo,
            acao=acao_jogador,
            tipo_habilidade=tipo_habilidade
        )

        # ---------------- Inimigo ----------------
        resultado_inimigo = None
        if self.inimigo.esta_vivo():
            habilidades = self.inimigo.habilidades_disponiveis()
            if habilidades:
                habilidade_escolhida = random.choice(habilidades)
                resultado_inimigo = Executor.executar(
                    atacante=self.inimigo,
                    alvo=self.jogador,
                    acao=Acao.USAR_HABILIDADE,
                    tipo_habilidade=habilidade_escolhida.tipo
                )

        # ---------------- Próximo turno ----------------
        self.turno += 1
        return resultado_jogador, resultado_inimigo