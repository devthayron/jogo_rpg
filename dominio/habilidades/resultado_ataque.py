class ResultadoAtaque:
    def __init__(self,
        executado: bool,
        dano: int = 0,
        energia_gasta: int = 0,
        tipo: str = None,
        motivo_falha = None,
    ):
        self.executado = executado
        self.dano = dano
        self.energia_gasta = energia_gasta
        self.tipo = tipo
        self.motivo_falha = motivo_falha