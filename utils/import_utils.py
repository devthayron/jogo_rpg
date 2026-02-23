import importlib
import pkgutil
from pathlib import Path
from dominio.habilidades.base import Habilidade

def carregar_habilidades(pasta_raiz="dominio.habilidades"):
    """
    Varre recursivamente todas as subpastas de habilidades,
    importa todos os módulos, garantindo que os decorators sejam executados.
    """

    pacote = importlib.import_module(pasta_raiz)
    caminho = Path(pacote.__file__).parent

    def _importar_recursivo(caminho_atual, pacote_atual):
        for finder, nome, ispkg in pkgutil.iter_modules([str(caminho_atual)]):
            full_mod = f"{pacote_atual}.{nome}"
            importlib.import_module(full_mod)

            # Se for pacote, entra recursivamente
            if ispkg:
                sub_caminho = caminho_atual / nome
                _importar_recursivo(sub_caminho, full_mod)

    _importar_recursivo(caminho, pasta_raiz)