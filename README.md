# Sistema de Combate em Python (POO)

Sistema de combate em Python orientado a objetos, evoluindo gradualmente como base para um RPG com IA.

## Objetivo do projeto

Criar uma base sólida de RPG em Python utilizando Programação Orientada a Objetos, com foco em modularidade, escalabilidade e organização de código.  

O projeto evoluiu para ter uma **base de habilidades centralizada**, permitindo que cada personagem tenha ataques próprios, incluindo ataque básico herdado por todos via decorator e fábrica de habilidades.

---

## Conceitos aplicados

* Programação Orientada a Objetos
* Herança e polimorfismo
* Encapsulamento de atributos
* Organização modular do código
* Separação de responsabilidades
* Validação centralizada de ataques e falhas
* via decorator e fábrica de habilidades

---

## Funcionalidades 

* Separação clara de responsabilidades: Personagem vs Habilidade  
* Decorator @registrar_habilidade_para registra habilidades para uma ou todas as classes
* Fábrica de personagens adiciona habilidades automaticamente
* Estrutura modular inicial para simulação de combate
* Código preparado para escalar e adicionar novas habilidades
* Base estruturada para futuras integrações com IA
* Sistema de falhas centralizado usando enums (`MotivoFalha`)  

---

## 📁 Estrutura do projeto


```
main.py -> inicia e executa o sistema

dominio/ -> Regras centrais e entidades do jogo
├─ personagens/
│  ├─ personagem.py
│  ├─ guerreiro.py
│  └─ arqueiro.py
├─ habilidades/
│  ├─ base.py -> classe base Habilidade
│  ├─ decorator.py -> registra habilidades automaticamente
│  ├─ guerreiro/
│  │  └─ golpe_pesado.py
│  ├─ arqueiro/
│  │  └─ disparo_triplo.py
│  └─ ataque_basico.py
├─ resultados/
│  └─ resultado_ataque.py
└─ enums/
   ├─ classe_personagem.py
   ├─ tipo_habilidade.py
   └─ motivo_falha.py

sistema/ -> Orquestra o funcionamento do combate
├─ acoes.py
├─ executor.py
└─ batalha.py

interface/ -> Camada de interação com o usuário
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

* Expandir o sistema de combate e ações (acoes.py, executor.py, batalha.py)
* Evoluir a interface Visual Utilizando a biblioteca `Pygame`
* Evoluir o terminal para melhor interação com usuário e exibição de habilidades 
* Adicionar novos tipos de personagem e habilidades facilmente via decorator
* Preparar a arquitetura para futura implementação de IA de decisão baseada no estado da batalha  

---

## 🧑‍💻 Autor

- **Thayron** (Desenvolvedor) – [LinkedIn](https://www.linkedin.com/in/thayron-higlander) 