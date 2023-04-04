import pygame
import sys
import numpy as np
import math
import random

# Definir cores
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Definir tamanho da tela
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
size = (WIDTH, HEIGHT)

# Inicializar Pygame
pygame.init()

# Criar a tela
screen = pygame.display.set_mode(size)

# Definir título da janela
pygame.display.set_caption("Connect 4")

# Criar tabuleiro vazio
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Inserir ficha no tabuleiro
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Verificar se a coluna está disponível
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# Encontrar a próxima linha disponível
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Imprimir o tabuleiro na tela
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), int(SQUARE_SIZE/2-5))

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), int(SQUARE_SIZE/2-5))
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), int(SQUARE_SIZE/2-5))

    pygame.display.update()

# Verificar se a jogada é vencedora
def winning_move(board, piece):
    # Verificar linhas horizontais
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Verificar linhas verticais
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Verificar linhas horizontais
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Verificar diagonais ascendentes
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Verificar diagonais descendentes
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

board = create_board()
game_over = False
turn = 0

draw_board(board)

while not game_over:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Jogador 1
            if turn == 0:
                col = int(event.pos[0] / SQUARE_SIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("Jogador 1 ganhou!")
                        game_over = True

            # Jogador 2
            else:
                col = random.randint(0, COLUMN_COUNT - 1)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        print("Jogador 2 ganhou!")
                        game_over = True

            turn += 1
            turn %= 2

            draw_board(board)

def Annealing(board, player, temperature):
    # Define a função de custo
    def cost_function(board, player, move):
        # Faça aqui a avaliação da qualidade da jogada (quanto maior o valor, melhor)
        # Por exemplo, pode-se utilizar uma função que calcula a chance de vitória do jogador
        # após realizar a jogada 'move' no tabuleiro 'board'
        return 0.0

    # Define a temperatura inicial (geralmente, é uma boa ideia escolher um valor alto)
    T = temperature
    
    # Define o fator de resfriamento (geralmente, é uma boa ideia escolher um valor próximo de 1)
    cooling_factor = 0.95
    
    # Define o número máximo de iterações
    max_iterations = 10000
    
    # Inicializa a jogada atual
    current_move = None
    
    # Inicializa a melhor jogada encontrada até agora
    best_move = None
    
    # Inicializa o valor da função de custo da melhor jogada encontrada até agora
    best_cost = float('-inf')
    
    # Executa o Simulated Annealing
    for i in range(max_iterations):
        # Escolhe uma jogada aleatória
        current_move = random.choice(range(len(board[0])))
        
        # Calcula o valor da função de custo da jogada atual
        current_cost = cost_function(board, player, current_move)
        
        # Verifica se a jogada atual é melhor do que a melhor jogada encontrada até agora
        if current_cost > best_cost:
            best_move = current_move
            best_cost = current_cost
        
        # Calcula a probabilidade de aceitar uma jogada pior
        p = math.exp((current_cost - best_cost) / T)
        
        # Gera um número aleatório entre 0 e 1
        r = random.uniform(0, 1)
        
        # Verifica se aceita a jogada pior
        if r < p:
            best_move = current_move
            best_cost = current_cost
        
        # Resfria a temperatura
        T *= cooling_factor
    
    return best_move

