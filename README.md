
# Jogo Connect 4 com IA de Simulated Annealing
- Esta é uma implementação em Python do jogo clássico Connect 4, aprimorada com um oponente de inteligência artificial (IA) que utiliza o algoritmo Simulated Annealing para decidir seus movimentos. O jogo foi desenvolvido utilizando a biblioteca pygame para a interface gráfica.

# Descrição
- Connect 4 é um jogo de tabuleiro para dois jogadores, onde cada jogador alterna a vez de soltar suas peças coloridas de cima para baixo em uma grade vertical. O objetivo é conectar quatro de suas próprias peças da mesma cor consecutivamente em uma linha, coluna ou diagonal, antes que o oponente o faça.

# Requisitos
Para executar o jogo, é necessário ter o Python instalado em seu sistema, juntamente com a biblioteca pygame. Você pode instalar o pygame usando o seguinte comando:

```bash
pip install pygame
```

# Como Jogar
Execute o script usando seu interpretador Python.
1. A janela do jogo será aberta, exibindo um tabuleiro Connect 4 vazio.
2. Os jogadores fazem suas jogadas clicando na coluna onde desejam soltar sua peça. A peça cairá na posição mais baixa disponível na coluna escolhida.
3. O primeiro jogador a conectar quatro de suas peças consecutivamente (horizontalmente, verticalmente ou diagonalmente) vence o jogo.
4. O jogo termina quando um jogador vence ou todo o tabuleiro é preenchido sem um vencedor.
   
# IA com Simulated Annealing
- Esta implementação inclui um oponente de IA que utiliza o algoritmo Simulated Annealing para fazer suas jogadas. A IA avalia as jogadas potenciais com base em um sistema de pontuação que considera sequências de suas próprias peças. Ela busca maximizar sua pontuação usando o Simulated Annealing, o que permite tomar decisões inteligentes enquanto explora diversas possibilidades.
