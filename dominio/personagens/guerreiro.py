from dominio.personagens.personagem import Personagem
from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.guerreiro.golpe_pesado import GolpePesado
from dominio.enums.tipo_habilidade import TipoHabilidade

class Guerreiro(Personagem):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida, dano)
        # Registra as habilidades do Guerreiro
        self.habilidades = [
            AtaqueBasico(self),  # Ataque básico universal
            GolpePesado(self)    # Habilidade especial do Guerreiro
        ]

    def ataque_especial(self, alvo: Personagem):
        """Executa a habilidade especial do Guerreiro"""
        return self.usar_habilidade(alvo, TipoHabilidade.GOLPE_PESADO)