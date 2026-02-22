#  Sistema de Combate em Python (POO)

Sistema de combate em Python orientado a objetos, evoluindo gradualmente como base para um RPG com IA.

##  Objetivo do projeto

Criar uma base sólida de RPG em Python utilizando Programação Orientada a Objetos, com foco em modularidade, escalabilidade e organização de código.  

O projeto evoluirá gradualmente de um sistema de combate simples para um RPG completo expandindo para mecânicas mais complexas

---

##  Conceitos aplicados

* Programação Orientada a Objetos
* Herança e polimorfismo
* Encapsulamento de atributos
* Organização modular do código
* Separação de responsabilidades

---

##  Funcionalidades 

* Separação clara de responsabilidades  
* Estrutura modular inicial para simulação de combate
* Código preparado para escalar 
* Base estruturada para futuras integrações com IA  

---

## 📁 Estrutura do projeto

```
main.py     -> inicia e executa o sistema

dominio/    -> Regras centrais e entidades do jogo
├─ personagens/
├─ habilidades/

sistema/    -> Orquestra o funcionamento do combate.
├─ acoes.py
├─ executor.py
└─ batalha.py

interface/  -> Camada de interação com o usuário
└─ terminal/
```

---

## Como executar

1. Clone o repositório
2. Execute o arquivo principal:

```bash
python main.py
```

---

## Próximos passos do projeto

* Implementar a camada de sistema (`acoes.py`, `executor.py`, `batalha.py`) 
* `batalha.py`: Criar o sistema de turnos, definindo ordem de ação e encerramento automático da batalha  
* `executor.py`: Estruturar um executor responsável por aplicar ações e registrar seus resultados  
* `acoes.py`: Evoluir o modelo de ações para permitir habilidades independentes do personagem  
* Desenvolver a interface textual no terminal para interação e visualização dos resultados  
* Evoluir a interface Visual Utilizando a biblioteca `Pygame`
* Preparar a arquitetura para futura implementação de IA de decisão baseada no estado da batalha  

---

## 🧑‍💻 Autor

- **Thayron** (Desenvolvedor) – [LinkedIn](https://www.linkedin.com/in/thayron-higlander) 