from dominio.personagens.guerreiro import Guerreiro
from dominio.personagens.arqueiro import Arqueiro
from dominio.enums.tipo_habilidade import TipoHabilidade

def mostrar_status(msg, personagem1, personagem2, resultado=None):
    if resultado:
        print(msg, resultado.__dict__)
    else:
        print(msg)
    print(personagem1)
    print(personagem2)
    print('---'*45)

def main():
    guerreiro = Guerreiro("Conan", vida=100, dano=15)
    arqueiro = Arqueiro("Legolas", vida=80, dano=12)

    mostrar_status("Status inicial:", guerreiro, arqueiro)

    resultado = guerreiro.usar_habilidade(arqueiro, TipoHabilidade.ATAQUE_BASICO)
    mostrar_status("Ataque Básico Guerreiro:", guerreiro, arqueiro, resultado)

    resultado = guerreiro.ataque_especial(arqueiro)
    mostrar_status("Golpe Pesado Guerreiro:", guerreiro, arqueiro, resultado)

    resultado = arqueiro.usar_habilidade(guerreiro, TipoHabilidade.ATAQUE_BASICO)
    mostrar_status("Ataque Básico Arqueiro:", guerreiro, arqueiro, resultado)

    resultado = arqueiro.ataque_especial(guerreiro)
    mostrar_status("Disparo Triplo Arqueiro:", guerreiro, arqueiro, resultado)

    arqueiro._energia = 0
    resultado = arqueiro.usar_habilidade(guerreiro, TipoHabilidade.ATAQUE_BASICO)
    mostrar_status("Ataque Arqueiro sem energia:", guerreiro, arqueiro, resultado)

if __name__ == "__main__":
    main()