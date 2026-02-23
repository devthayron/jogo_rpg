from abc import ABC
from typing import Dict, List

from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.motivo_falha import MotivoFalha
from dominio.enums.classe_personagem import ClassePersonagem


class Personagem(ABC):

    def __init__(
        self,
        nome: str,
        vida: int,
        dano: int,
        classe: ClassePersonagem,
        energia_max: int = 100
    ):
        self.nome = nome
        self.classe = classe

        self._vida_max = vida
        self._vida = vida

        self._energia_max = energia_max
        self._energia = energia_max

        self.dano = dano

        self._habilidades: Dict[TipoHabilidade, object] = {}

    # ---------------- PROPERTIES ----------------

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        self._vida = max(0, min(valor, self._vida_max))

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor: int):
        self._energia = max(0, min(valor, self._energia_max))

    # ---------------- ESTADO ----------------

    def esta_vivo(self) -> bool:
        return self._vida > 0

    # ---------------- RECURSOS ----------------

    def gastar_energia(self, custo: int):
        if custo > self._energia:
            raise ValueError("Energia insuficiente")
        self.energia -= custo

    def receber_dano(self, dano: int):
        self.vida -= dano

    def regenerar_vida(self, valor: int = None, percentual: float = None):
        if valor is None and percentual is None:
            raise ValueError("Informe valor ou percentual")

        if percentual is not None:
            valor = int(self._vida_max * percentual)

        self.vida += valor

    def regenerar_energia(self, valor: int = None, percentual: float = None):
        if valor is None and percentual is None:
            raise ValueError("Informe valor ou percentual")

        if percentual is not None:
            valor = int(self._energia_max * percentual)

        self.energia += valor

    # ---------------- HABILIDADES ----------------

    def adicionar_habilidade(self, habilidade):
        self._habilidades[habilidade.tipo] = habilidade

    def usar_habilidade(self, alvo: "Personagem", tipo: TipoHabilidade) -> ResultadoAtaque:
        habilidade = self._habilidades.get(tipo)

        if not habilidade:
            return ResultadoAtaque(
                executado=False,
                motivo_falha=MotivoFalha.HABILIDADE_INEXISTENTE,
                tipo=tipo
            )

        # 🔥 CORREÇÃO AQUI:
        # Não passamos self, pois a habilidade já conhece o personagem
        return habilidade.executar(alvo)

    def listar_habilidades(self) -> List[str]:
        return [tipo.name for tipo in self._habilidades.keys()]

    def habilidades_disponiveis(self):
        return list(self._habilidades.values())

    # ---------------- DEBUG ----------------

    def __str__(self):
        habilidades = ", ".join(self.listar_habilidades())
        return (
            f"{self.nome} | "
            f"HP {self.vida}/{self._vida_max} | "
            f"EN {self.energia}/{self._energia_max} | "
            f"Habilidades: {habilidades}"
        )