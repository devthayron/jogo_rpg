from sistema.acoes import Acao


class Executor:

    @staticmethod
    def executar(atacante, alvo, acao, tipo_habilidade=None):

        if acao == Acao.USAR_HABILIDADE:

            if tipo_habilidade is None:
                raise ValueError("Tipo de habilidade não pode ser None.")

            return atacante.usar_habilidade(alvo, tipo_habilidade)

        if acao == Acao.PASSAR_TURNO:
            return None

        raise ValueError(f"Ação desconhecida: {acao}")