from dominio.personagens.guerreiro import Guerreiro
from dominio.personagens.arqueiro import Arqueiro
from dominio.fabrica.fabrica_habilidade import FabricaHabilidade
from dominio.enums.classe_personagem import ClassePersonagem

class FabricaPersonagem:
    """
    Fábrica que cria personagens e adiciona automaticamente
    todas as habilidades registradas para a classe.
    """

    CLASSES = {
        ClassePersonagem.GUERREIRO: Guerreiro,
        ClassePersonagem.ARQUEIRO: Arqueiro,
    }

    @staticmethod
    def criar(classe: ClassePersonagem, nome: str):
        if classe not in FabricaPersonagem.CLASSES:
            raise ValueError("Classe inválida")

        # Cria a instância do personagem
        personagem = FabricaPersonagem.CLASSES[classe](nome)

        # 🔥 Adiciona todas as habilidades registradas para a classe
        habilidades_cls = FabricaHabilidade._registro.get(classe, {}).values()
        for hab_cls in habilidades_cls:
            personagem.adicionar_habilidade(hab_cls(personagem))

        return personagem