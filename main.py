from dominio.personagens.guerreiro import Guerreiro
from dominio.personagens.arqueiro import Arqueiro

arthur = Guerreiro("Arthur", 200, 20)
legolas = Arqueiro("Legolas", 150, 15)

# Ataque normal
res1 = arthur.atacar(legolas)
print(f"{arthur.nome} atacou {legolas.nome}: {res1.dano} de dano | Tipo: {res1.tipo}")

# Ataque especial
res2 = legolas.ataque_especial(arthur)
print(f"{legolas.nome} atacou {arthur.nome}: {res2.dano} de dano | Tipo: {res2.tipo}")

print(arthur)
print(legolas)