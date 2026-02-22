from dominio.personagens.personagem import Personagem
from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.arqueiro.disparo_triplo import DisparoTriplo
from dominio.enums.tipo_habilidade import TipoHabilidade

class Arqueiro(Personagem):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida, dano)
        # Registra as habilidades do Arqueiro
        self.habilidades = [
            AtaqueBasico(self),   # Ataque básico universal
            DisparoTriplo(self)    # Habilidade especial do Arqueiro
        ]

    def ataque_especial(self, alvo: Personagem):
        """Executa a habilidade especial do Arqueiro"""
        return self.usar_habilidade(alvo, TipoHabilidade.DISPARO_TRIPLO)