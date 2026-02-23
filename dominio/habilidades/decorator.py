from dominio.fabrica.fabrica_habilidade import FabricaHabilidade
from dominio.enums.classe_personagem import ClassePersonagem

def registrar_habilidade_para(*classes: ClassePersonagem):
    def wrapper(cls):
        alvo_classes = classes if classes else list(ClassePersonagem)
        for c in alvo_classes:
            FabricaHabilidade.registrar(c, cls)
        return cls
    return wrapper