# Grafos2_Labirinto

**Conteúdo da Disciplina**: Grafos 1

## 👥 Alunos
| Matrícula     | Aluno                             |
| ------------- | ---------------------------------- |
| 22/2006196    | Wallyson Paulo Costa Souza         |
| 22/2006893    | Kaio Macedo Santana                |

---

## 📌 Sobre
Este projeto é uma **simulação interativa de um jogo de labirinto**, que utiliza conceitos de grafos para a geração e resolução de caminhos.  
O labirinto é gerado utilizando o algoritmo de **Prim**, e a rota do início ao fim é calculada com o **algoritmo de Dijkstra** para encontrar o menor caminho possível (em versões futuras).

---

## 🛠️ Instalação

**Linguagem:** Python  
**Biblioteca:** Pygame  

### Pré-requisitos:
- Python 3.8 ou superior
- Pygame

### Passos:

1. Clone este repositório:
```bash
git clone https://github.com/projeto-de-algoritmos-2025/Grafos2__
```

2. Acesse o diretório do projeto:
```bash
cd Grafos2__
```

3. Instale as dependências:
```bash
pip install pygame
```

4. Execute o jogo:
```bash
python jogo.py
```

---

## 🎮 Uso

O jogador deve percorrer o labirinto do **início (azul)** até o **fim (vermelho)** utilizando as teclas direcionais. Ao completar o labirinto, o jogo exibe uma mensagem de vitória e oferece a opção de reiniciar ou sair.

### Controles:
- 🔼 **Seta para cima** – mover para cima  
- 🔽 **Seta para baixo** – mover para baixo  
- ◀️ **Seta para esquerda** – mover para a esquerda  
- ▶️ **Seta para direita** – mover para a direita  
- 🔁 **R** – jogar novamente  
- ❌ **ESC** – sair do jogo

---

## 🧠 Como Funciona

O jogo implementa os seguintes componentes principais:

- **Geração do labirinto:**  
  Utiliza o **algoritmo de Prim** para criar um labirinto aleatório com caminhos únicos e conexos.

- **Visualização:**  
  O labirinto é desenhado com Pygame, com destaque visual para:
  - Ponto de início (azul)
  - Ponto de chegada (vermelho)
  - Jogador (verde)

- **Interação:**  
  O jogador se movimenta com as teclas e precisa encontrar a saída do labirinto.

---

## 🌟 Características

- Labirinto gerado aleatoriamente
- Gráficos simples e funcionais com Pygame
- Mensagem de vitória ao completar o labirinto
- Opção de reinício após vencer

---

## 📽️ Apresentação
Link da apresentação:

---
