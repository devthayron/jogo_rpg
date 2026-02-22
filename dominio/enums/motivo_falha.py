from enum import Enum, auto

class MotivoFalha(Enum):
    SEM_ENERGIA = auto()
    ALVO_MORTO = auto()
    ATACANTE_MORTO = auto()
    ALVO_INVALIDO = auto()
    HABILIDADE_INEXISTENTE = auto()