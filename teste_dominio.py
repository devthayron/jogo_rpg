from dominio.personagens.guerreiro import Guerreiro
from dominio.personagens.arqueiro import Arqueiro
from dominio.habilidades.base import AtaqueBasico
from dominio.habilidades.guerreiro.golpe_pesado import GolpePesado
from dominio.habilidades.arqueiro.disparo_triplo import DisparoTriplo

def main():
    # Criar personagens
    guerreiro = Guerreiro("Conan", vida=100, dano=15)
    arqueiro = Arqueiro("Legolas", vida=80, dano=12)

    # Adicionar habilidades
    ataque_basico_guerreiro = AtaqueBasico(guerreiro)
    golpe_pesado = GolpePesado(guerreiro)
    
    ataque_basico_arqueiro = AtaqueBasico(arqueiro)
    disparo_triplo = DisparoTriplo(arqueiro)

    # Mostrar status inicial
    print(guerreiro)
    print(arqueiro)
    print("---")

    # Teste 1: ataque básico do guerreiro no arqueiro
    resultado = ataque_basico_guerreiro.executar(arqueiro)
    print("Ataque Básico Guerreiro:", resultado.__dict__)
    print(guerreiro)
    print(arqueiro)
    print("---")

    # Teste 2: golpe pesado do guerreiro no arqueiro
    resultado = golpe_pesado.executar(arqueiro)
    print("Golpe Pesado Guerreiro:", resultado.__dict__)
    print(guerreiro)
    print(arqueiro)
    print("---")

    # Teste 3: ataque básico do arqueiro no guerreiro
    resultado = ataque_basico_arqueiro.executar(guerreiro)
    print("Ataque Básico Arqueiro:", resultado.__dict__)
    print(guerreiro)
    print(arqueiro)
    print("---")

    # Teste 4: disparo triplo do arqueiro no guerreiro
    resultado = disparo_triplo.executar(guerreiro)
    print("Disparo Triplo Arqueiro:", resultado.__dict__)
    print(guerreiro)
    print(arqueiro)
    print("---")

    # Teste 5: testar falha de energia
    arqueiro._energia = 0
    resultado = ataque_basico_arqueiro.executar(guerreiro)
    print("Ataque Arqueiro sem energia:", resultado.__dict__)

if __name__ == "__main__":
    main()