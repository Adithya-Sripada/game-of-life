import random

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

print(random_state(2, 5))