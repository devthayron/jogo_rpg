from dominio.personagens.personagem import Personagem
from dominio.habilidades.resultado_ataque import ResultadoAtaque
from dominio.habilidades.tipo_ataque import TipoAtaque
import random 

class Arqueiro(Personagem):
    
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida, dano)

    def atacar(self, alvo, custo = 20, dano_especial = None):
        return super().atacar(alvo, custo, dano_especial)

    def ataque_especial(self,alvo: Personagem):
        super().ataque_especial(alvo)
        dano_triplo = 0
        for _ in range(3):
            dano = self.dano // 2 if random.random() <= 0.5 else self.dano
            dano_triplo += dano
        resultado = self.atacar(alvo , custo=45 , dano_especial=dano_triplo, tipo=TipoAtaque.DANO_TRIPLO)
        return resultado