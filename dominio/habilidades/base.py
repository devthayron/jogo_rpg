from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.motivo_falha import MotivoFalha
from dominio.personagens.personagem import Personagem
from abc import ABC,abstractmethod

class Habilidade(ABC):
    """Classe base para todas as habilidades"""

    def __init__(self, personagem):
        self.personagem = personagem
        self.tipo = TipoHabilidade.ATAQUE_BASICO
        self.custo = 20  # padrão, subclasses podem sobrescrever

    def validar(self, alvo):
        """Valida se a habilidade pode ser executada"""
        if not isinstance(alvo, Personagem):
            return False, MotivoFalha.ALVO_INVALIDO
        if not self.personagem.esta_vivo():
            return False, MotivoFalha.ATACANTE_MORTO
        if not alvo.esta_vivo():
            return False, MotivoFalha.ALVO_MORTO
        if self.personagem.energia < self.custo:
            return False, MotivoFalha.SEM_ENERGIA
        return True, None

    def executar(self, alvo):
        """Executa a habilidade"""
        valido, motivo = self.validar(alvo)
        if not valido:
            return ResultadoAtaque(
                executado=False,
                motivo_falha=motivo,
                tipo=self.tipo
            )
        return self._executar_ataque(alvo)

    # ----------------- Método abstrato -----------------
    @abstractmethod
    def _executar_ataque(self, alvo): 
        """Subclasses devem implementar a lógica do ataque"""
        pass

# ----------------- Ataque Básico -----------------
class AtaqueBasico(Habilidade):
    """Todos os personagens possuem ataque básico"""
    
    def __init__(self, personagem) -> ResultadoAtaque:
        super().__init__(personagem)
        self.tipo = TipoHabilidade.ATAQUE_BASICO
        self.custo = 20  # custo padrão de energia

    def _executar_ataque(self, alvo):
        self.personagem.gastar_energia(self.custo)
        dano_final = self.personagem.dano
        alvo.receber_dano(dano_final)
        return ResultadoAtaque(
            executado=True,
            dano=dano_final,
            energia_gasta=self.custo,
            tipo=self.tipo
        )