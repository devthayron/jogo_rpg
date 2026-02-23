from dominio.enums.classe_personagem import ClassePersonagem

class FabricaHabilidade:
    _registro = {}  # {ClassePersonagem: {nome_habilidade: ClasseHabilidade}}

    @classmethod
    def registrar(cls, personagem_classe: ClassePersonagem, habilidade_cls):
        if personagem_classe not in cls._registro:
            cls._registro[personagem_classe] = {}
        cls._registro[personagem_classe][habilidade_cls.__name__] = habilidade_cls
        print(f"[FabricaHabilidade] Registrado {habilidade_cls.__name__} para {personagem_classe.value}")

    @classmethod
    def criar(cls, personagem, nome_habilidade: str):
        personagem_classe = personagem.classe
        if personagem_classe not in cls._registro:
            raise ValueError(f"Nenhuma habilidade registrada para {personagem_classe.value}")
        habilidade_cls = cls._registro[personagem_classe].get(nome_habilidade)
        if not habilidade_cls:
            raise ValueError(f"Habilidade {nome_habilidade} não registrada para {personagem_classe.value}")
        return habilidade_cls(personagem)