from abc import ABC, abstractmethod
from dominio.resultados.resultado_ataque import ResultadoAtaque
from dominio.enums.tipo_habilidade import TipoHabilidade
from dominio.enums.motivo_falha import MotivoFalha
from dominio.personagens.personagem import Personagem
from dominio.habilidades.decorator import registrar_habilidade_para




class Habilidade(ABC):
    """
    Classe base de todas as habilidades.
    Cada habilidade deve implementar o método _executar.
    """

    def __init__(self, personagem: Personagem):
        self.personagem = personagem
        self.tipo: TipoHabilidade = None
        self.custo: int = 0

    def validar(self, alvo: Personagem):
        """
        Valida se a habilidade pode ser executada.
        Retorna (True, None) se válido, caso contrário retorna (False, MotivoFalha)
        """
        if not isinstance(alvo, Personagem):
            return False, MotivoFalha.ALVO_INVALIDO

        if not self.personagem.esta_vivo():
            return False, MotivoFalha.ATACANTE_MORTO

        if not alvo.esta_vivo():
            return False, MotivoFalha.ALVO_MORTO

        if self.personagem.energia < self.custo:
            return False, MotivoFalha.SEM_ENERGIA

        return True, None

    def executar(self, alvo: Personagem) -> ResultadoAtaque:
        """
        Executa a habilidade, aplicando validações.
        Retorna um objeto ResultadoAtaque com sucesso ou falha.
        """
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
        """
        Implementação específica da habilidade.
        Deve gastar energia, calcular dano e retornar ResultadoAtaque.
        """
        pass



@registrar_habilidade_para()
class AtaqueBasico(Habilidade):
    """
    Habilidade básica comum a todas as classes.
    """

    def __init__(self, personagem: Personagem):
        super().__init__(personagem)
        self.tipo = TipoHabilidade.ATAQUE_BASICO
        self.custo = 20

    def _executar(self, alvo: Personagem) -> ResultadoAtaque:
        # Gasta energia do personagem
        self.personagem.gastar_energia(self.custo)

        # Calcula dano final
        dano_final = self.personagem.dano
        alvo.receber_dano(dano_final)

        # Retorna resultado
        return ResultadoAtaque(
            executado=True,
            dano=dano_final,
            energia_gasta=self.custo,
            tipo=self.tipo
        )