from dominio.personagens.personagem import Personagem
from dominio.enums.classe_personagem import ClassePersonagem


class Guerreiro(Personagem):

    def __init__(self, nome: str, vida: int = 150, dano: int = 25):
        super().__init__(
            nome=nome,
            vida=vida,
            dano=dano,
            classe=ClassePersonagem.GUERREIRO
        )