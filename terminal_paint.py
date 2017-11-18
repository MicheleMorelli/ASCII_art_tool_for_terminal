from getch_class import *

def clean_screen():
    print("\n"*120)

def draw_grid(grid):
    for row in grid:
        print(*row, sep = '')


canvas = [[' ' for i in range(32)] for k in range(16)]
cursor = [0,0]
mode = 'write'
inp = 'g'
while inp != 'q':
    if inp == 'a':
        cursor[0] -= 1
    elif inp == 'd':
        cursor[0] += 1
    elif inp == 'w':
        cursor[1] -= 1
    elif inp == 's':
        cursor[1] += 1
    elif inp == 'm':
        if mode != 'write':
            mode = 'write'
        else:
            mode = 'move'
    x = cursor[1]
    y = cursor[0]
    if mode == 'write':
        canvas[x][y] = '#'
    clean_screen()
    draw_grid(canvas)
    inp = getch()

