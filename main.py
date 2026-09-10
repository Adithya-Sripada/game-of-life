import random
import sys

import pygame
import time

def null_state(width, height):
    return [[0 for x in range(width)] for y in range(height)]

def board_from_file(filename):
    board = []
    f = open(filename)
    row = []
    for c in f:
        for i in c:
            if i != '\n':
                row.append(int(i))
        board.append(row)
        row = []
    return board



def random_state(width, height):
    board = null_state(width, height)
    n = random.random()
    for r in range(height):
        for c in range(width):
            board[r][c] = round(n)
            n = random.random()
    return board

def render(board):
    pygame.display.init()
    width = len(board[0])*100
    height = len(board)*100
    b = pygame.display.set_mode((width, height))
    x = 0
    y = 0
    for row in board:
        for col in row:
            rect = pygame.Rect((x, y), (100, 100))
            if col:
                pygame.draw.rect(b, (255, 255 , 255), rect)
            else:
                pygame.draw.rect(b, (0, 0, 0), rect)
            x += 100
        y += 100
        x = 0

    pygame.display.update()

def console_render(board):
    DEAD = '\033[31m'
    ALIVE = '\033[92m'
    RESET = '\033[0m'
    for row in board:
        for col in row:
            if col:
                print(ALIVE + 'A' + RESET, end=' ')
            else:
                print(DEAD + 'D' + RESET,end=' ')
        print('\n')
    print(RESET)

def update_cell(neighbors, r, c, board):
    if board[r][c] == 1:
        if neighbors.count(1) <= 1:
            return 0
        elif 2 <= neighbors.count(1) <= 3:
            return 1
        elif neighbors.count(1) > 3:
            return 0
    else:
        if neighbors.count(1) == 3:
            return 1
        return 0


def next_edges(board):
    new_edges = null_state(len(board[0]), len(board))
    for c in range(1, len(board[0])-1):
        r = 0
        neighbors = [board[r][c - 1], board[r][c + 1], board[r+1][c - 1], board[r+1][c], board[r+1][c + 1]]
        new_edges[r][c] = update_cell(neighbors, r, c, board)

    for c in range(1, len(board[0])-1):
        r = len(board)-1
        neighbors = [board[r - 1][c - 1], board[r - 1][c], board[r - 1][c + 1], board[r][c - 1], board[r][c + 1]]
        new_edges[r][c] = update_cell(neighbors, r, c, board)

    for r in range(1, len(board)-1):
        c = 0
        neighbors = [board[r - 1][c], board[r - 1][c + 1], board[r][c + 1], board[r + 1][c], board[r + 1][c + 1]]
        new_edges[r][c] = update_cell(neighbors, r, c, board)

    for r in range(1, len(board)-1):
        c = len(board[0])-1
        neighbors = [board[r - 1][c - 1], board[r - 1][c], board[r][c - 1], board[r + 1][c - 1], board[r + 1][c]]
        new_edges[r][c] = update_cell(neighbors, r, c, board)

    neighbors = [board[0][1], board[1][0], board[1][1]]
    new_edges[0][0] = update_cell(neighbors, 0, 0, board)

    neighbors = [board[0][len(board[0])-2], board[1][len(board[0])-2], board[1][len(board[0])-1]]
    new_edges[0][len(board[0])-1] = update_cell(neighbors, 0, len(board[0])-1, board)

    neighbors = [board[len(board)-1][1], board[len(board)-2][0], board[len(board)-2][1]]
    new_edges[len(board)-1][0] = update_cell(neighbors, len(board)-1, 0, board)

    neighbors = [board[len(board)-1][len(board[0])-2], board[len(board)-2][len(board[0])-1], board[len(board)-2][len(board[0])-2]]
    new_edges[len(board)-1][len(board[0])-1] = update_cell(neighbors, len(board)-1, len(board[0])-1, board)

    return new_edges


def next_state(board):
    new_board = next_edges(board)
    neighbors = []
    for r in range(1, len(board)-1):
        for c in range(1, len(board[r])-1):
            neighbors = [board[r-1][c-1], board[r-1][c], board[r-1][c+1], board[r][c-1], board[r][c+1], board[r+1][c-1], board[r+1][c], board[r+1][c+1]]
            new_board[r][c] = update_cell(neighbors, r, c, board)

    return new_board

if __name__ == '__main__':
    '''
        Usage: 
        python main.py <filename> to start from a non-random state
        else: python main.py
    '''
    if len(sys.argv) > 1:
        board = board_from_file(sys.argv[1])
    else:
        board = random_state(9, 9)
    pygame.init()
    while True:
        render(board)
        time.sleep(3)
        board = next_state(board)

