from dominio.habilidades.base import Habilidade
from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade


class GolpePesado(Habilidade):

    def __init__(self, personagem):
        super().__init__(personagem)
        self.tipo = TipoHabilidade.GOLPE_PESADO
        self.custo = 40

    def _executar(self, alvo):
        self.personagem.gastar_energia(self.custo)

        dano_final = self.personagem.dano * 2
        alvo.receber_dano(dano_final)

        return ResultadoAtaque(
            executado=True,
            dano=dano_final,
            energia_gasta=self.custo,
            tipo=self.tipo
        )