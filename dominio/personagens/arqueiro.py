from dominio.personagens.personagem import Personagem
from dominio.enums.classe_personagem import ClassePersonagem


class Arqueiro(Personagem):

    def __init__(self, nome: str, vida: int = 120, dano: int = 20):
        super().__init__(
            nome=nome,
            vida=vida,
            dano=dano,
            classe=ClassePersonagem.ARQUEIRO
        )