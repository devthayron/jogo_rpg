from dominio.habilidades.resultado_ataque import ResultadoAtaque
from dominio.habilidades.tipo_ataque import TipoAtaque
from abc import ABC, abstractmethod

class Personagem(ABC):
    
    def __init__(self,nome: str,vida: int,dano: int, energia_max: int = 100):
        self.nome = nome
        self._vida_max = vida
        self._vida = vida
        self._energia = energia_max
        self._energia_max = energia_max
        self.dano = dano

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

    # ---------------- Métodos ----------------

    def esta_vivo(self):
        return self._vida > 0
    
    def gastar_energia(self,custo: int):
        self.energia -= custo 

    def receber_dano(self,dano):
        self.vida -= dano

    def regenerar_vida(self,valor: int=20):
        self.vida += valor

    def regenerar_energia(self,valor: int=10):
        self.energia += valor
    
    def validar_ataque(self,alvo: 'Personagem',custo):

        if not isinstance(alvo,Personagem):
            raise TypeError('Alvo precisa ser um Personagem')

        if not self.esta_vivo():
            return False, 'ATACANTE_MORTO'
        
        if not alvo.esta_vivo():
            return False, 'ALVO_MORTO'

        if self.energia < custo:
            return False, 'SEM_ENERGIA'
        
        return True, None

    def atacar(self,alvo: 'Personagem', custo: int=20,
               dano_especial: int=None,
               tipo=TipoAtaque.BASICO) -> ResultadoAtaque:

        valido, motivo = self.validar_ataque(alvo,custo)

        if not valido:
            return ResultadoAtaque(
                executado=False,
                motivo_falha=motivo
            )

        self.gastar_energia(custo)

        dano_final = self.dano if dano_especial is None else dano_especial

        alvo.receber_dano(dano_final)

        return ResultadoAtaque(
            executado=True,
            dano=dano_final,
            energia_gasta=custo,
            tipo=tipo
            )

    @abstractmethod
    def ataque_especial(self,alvo: 'Personagem') -> ResultadoAtaque:
        pass

    def __str__(self):
        return(f'{self.nome} | HP {self._vida}/{self._vida_max} | EN {self._energia}')