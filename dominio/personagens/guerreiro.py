from dominio.personagens.personagem import Personagem
from dominio.habilidades.resultado_ataque import ResultadoAtaque
from dominio.habilidades.tipo_ataque import TipoAtaque

class Guerreiro(Personagem):
    
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida, dano)

    def atacar(self, alvo, custo = 20, dano_especial = None):
        return super().atacar(alvo, custo, dano_especial)

    def ataque_especial(self,alvo: Personagem):
        super().ataque_especial(alvo)
        golpe_pesado = self.dano * 2
        resultado = self.atacar(alvo ,custo=40,dano_especial=golpe_pesado,tipo=TipoAtaque.GOLPE_PESADO)
        return resultado