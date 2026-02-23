import random
from dominio.habilidades.decorator import registrar_habilidade_para
from dominio.habilidades.base import Habilidade
from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.classe_personagem import ClassePersonagem

@registrar_habilidade_para(ClassePersonagem.ARQUEIRO)
class DisparoTriplo(Habilidade):

    def __init__(self, personagem):
        super().__init__(personagem)
        self.tipo = TipoHabilidade.DISPARO_TRIPLO
        self.custo = 45

    def _executar(self, alvo):
        self.personagem.gastar_energia(self.custo)

        dano_total = 0

        for _ in range(3):
            if random.random() <= 0.5:
                dano = self.personagem.dano // 2
            else:
                dano = self.personagem.dano

            dano_total += dano

        alvo.receber_dano(dano_total)

        return ResultadoAtaque(
            executado=True,
            dano=dano_total,
            energia_gasta=self.custo,
            tipo=self.tipo
        )