from dominio.personagens.personagem import Personagem
from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.arqueiro.disparo_triplo import DisparoTriplo
from dominio.enums.tipo_habilidade import TipoHabilidade

class Arqueiro(Personagem):
    def __init__(self, nome, vida, dano):
        # Cria lista de habilidades dinamicamente
        habilidades = [
            AtaqueBasico(None),  # Ataque universal
            DisparoTriplo(None)  # Habilidade especial do Arqueiro
        ]
        super().__init__(nome, vida, dano, habilidades=habilidades)
        # Conecta as habilidades ao personagem
        for hab in self.habilidades:
            hab.registrar_dono(self)

    def ataque_especial(self, alvo: Personagem):
        """Executa a habilidade especial do Arqueiro"""
        return self.usar_habilidade(alvo, TipoHabilidade.DISPARO_TRIPLO)