from dominio.habilidades.base import Habilidade
from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
import random

class DisparoTriplo(Habilidade):
    """Golpe especial do Arqueiro que ataca 3 vezes com chance de dano reduzido"""
    def __init__(self, personagem):
        super().__init__(personagem)
        self.tipo = TipoHabilidade.DISPARO_TRIPLO
        self.custo = 45  # custo de energia do disparo triplo

    def _executar_ataque(self, alvo):
        self.personagem.gastar_energia(self.custo)
        dano_total = 0
        for _ in range(3):
            dano = self.personagem.dano // 2 if random.random() <= 0.5 else self.personagem.dano
            dano_total += dano
        alvo.receber_dano(dano_total)
        return ResultadoAtaque(
            executado=True,
            dano=dano_total,
            energia_gasta=self.custo,
            tipo=self.tipo
        )