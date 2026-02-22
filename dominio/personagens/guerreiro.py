from dominio.personagens.personagem import Personagem
from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.guerreiro.golpe_pesado import GolpePesado
from dominio.enums.tipo_habilidade import TipoHabilidade

class Guerreiro(Personagem):
    def __init__(self, nome, vida, dano):
        # Cria lista de habilidades dinamicamente
        habilidades = [
            AtaqueBasico(None),  # Ataque universal
            GolpePesado(None)    # Habilidade especial do Guerreiro
        ]
        super().__init__(nome, vida, dano, habilidades=habilidades)
        # Conecta as habilidades ao personagem
        for hab in self.habilidades:
            hab.registrar_dono(self)

    def ataque_especial(self, alvo: Personagem):
        """Executa a habilidade especial do Guerreiro"""
        return self.usar_habilidade(alvo, TipoHabilidade.GOLPE_PESADO)