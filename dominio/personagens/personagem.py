from abc import ABC, abstractmethod
from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.motivo_falha import MotivoFalha

class Personagem(ABC):
    def __init__(self, nome: str, vida: int, dano: int, energia_max: int = 100, habilidades: list = None):
        self.nome = nome
        self._vida_max = vida
        self._vida = vida
        self._energia = energia_max
        self._energia_max = energia_max
        self.dano = dano
        self.habilidades = habilidades or []  # todas as habilidades do personagem

    # ---------------- Properties / Setters ----------------
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

    # ---------------- Métodos de status ----------------
    def esta_vivo(self):
        return self._vida > 0

    def gastar_energia(self, custo: int):
        self.energia -= custo

    def receber_dano(self, dano):
        self.vida -= dano

    def regenerar_vida(self, valor: int = None, percentual: float = None):
        if percentual is not None:
            valor = int(self._vida_max * percentual)
        self.vida += valor

    def regenerar_energia(self, valor: int = None, percentual: float = None):
        if percentual is not None:
            valor = int(self._energia_max * percentual)
        self.energia += valor


    def usar_habilidade(self, alvo: 'Personagem', tipo: TipoHabilidade) -> ResultadoAtaque:
        """Executa a habilidade de acordo com o tipo"""
        for hab in self.habilidades:
            if hab.tipo == tipo:
                return hab.executar(alvo)
        return ResultadoAtaque(executado=False, motivo=MotivoFalha.HABILIDADE_INEXISTENTE)

    def listar_habilidades(self):
        return [hab.tipo.name for hab in self.habilidades]
    
    def __str__(self):
        habs = ", ".join(self.listar_habilidades())
        return f'{self.nome} | HP {self.vida}/{self._vida_max} | EN {self.energia}/{self._energia_max} | Habilidades: {habs}'