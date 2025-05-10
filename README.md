
# Grafos2_Labirinto

**Conteúdo da Disciplina**: Grafos 1

## Alunos
| Matrícula   | Aluno                             |
|------------|-----------------------------------|
| 22/2006196 | Wallyson Paulo Costa Souza        |
| 22/2006893 | Kaio Macedo Santana               |

## Sobre  
Esta é uma implementação interativa de um labirinto gerado a partir de algoritmos clássicos de grafos — **Prim** e **Kruskal** — com visualização em tempo real e movimentação manual do jogador, do início ao fim do labirinto.

## Instalação  
**Linguagem**: Python  
**Framework**: Pygame

### Pré-requisitos
Certifique-se de ter o Python instalado (versão 3.6 ou superior) e o `pip` para gerenciar pacotes.

1. Clone este repositório:
   ```bash
   git clone https://github.com/projeto-de-algoritmos-2025/Grafos1_LabirintoPrimKruskal.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd Grafos1_LabirintoPrimKruskal
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install pygame
   ```

4. Execute o arquivo principal:
   ```bash
   python jogo.py
   ```

## Uso  
Após iniciar o programa, você verá um menu inicial com as opções de geração de labirinto:

- **P**: Gera um labirinto utilizando o algoritmo de **Prim**  
- **K**: Gera um labirinto utilizando o algoritmo de **Kruskal**

Durante o jogo:

- Setas direcionais: Movem o jogador (caminho manual)
- Fechar janela: Encerra o jogo

O objetivo é alcançar o quadrado de **chegada (verde)** a partir da **partida (azul)**, evitando as paredes do labirinto.

## Outros  

### Características

- Geração automática de labirinto com dois algoritmos: Prim e Kruskal
- Representação visual do labirinto com Pygame
- Controle manual do jogador
- Indicação gráfica de ponto de partida e chegada
- Mensagem de vitória ao completar o labirinto

### Como Funciona

O labirinto é representado como uma grade de células, onde:

- Cada célula é um nó no grafo
- As paredes representam a ausência de arestas
- O algoritmo **Prim** constrói uma árvore geradora mínima partindo de uma célula inicial
- O algoritmo **Kruskal** seleciona aleatoriamente arestas para conectar componentes até formar uma árvore geradora
- As paredes são removidas conforme as arestas são aceitas

O jogador se move célula a célula, respeitando as passagens disponíveis.

## Apresentação  
Link da apresentação:
