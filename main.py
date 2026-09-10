import random


class Colors:
    DEAD = '\033[31m'
    ALIVE = '\033[92m'
    RESET = '\033[0m'

def null_state(width, height):
    return [[0 for x in range(width)] for y in range(height)]

def random_state(width, height):
    board = null_state(width, height)
    n = random.random()
    for r in range(height):
        for c in range(width):
            board[r][c] = round(n)
            n = random.random()
    return board

def render(board):
    for row in board:
        for col in row:
            if col:
                print(Colors.ALIVE + 'A' + Colors.RESET, end=' ')
            else:
                print(Colors.DEAD + 'D' + Colors.RESET,end=' ')
        print('\n')
    print(Colors.RESET)


if __name__ == '__main__':
    render(random_state(30, 20))