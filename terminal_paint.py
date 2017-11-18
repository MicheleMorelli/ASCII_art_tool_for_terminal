from getch_class import *

def clean_screen():
    print("\n"*120)

def draw_grid(grid,width):
    print('_' * (width+2))
    for row in grid:
        print('|',end = '')
        print(*row,'|', sep = '')
    print('|' * (width + 2))


width = 64
height = 16

canvas = [[' ' for i in range(width)] for k in range(height)]
cursor = [0,0]
mode = 'move'
inp = 'g'
prev = ' '
while inp != 'q':
    x = cursor[1]
    y = cursor[0]
    if mode == 'move':
        canvas[x][y] = prev
        
    if inp == 'a':
        cursor[0] -= 1
    elif inp == 'd':
        cursor[0] += 1
    elif inp == 'w':
        cursor[1] -= 1
    elif inp == 's':
        cursor[1] += 1
    elif inp == 'm':
        if mode == 'write':
            mode = 'move'
        else:
            mode = 'write'
    x = cursor[1]
    y = cursor[0]
    if mode == 'write':
        canvas[x][y] = '#'
    elif mode == 'move':
        prev = canvas[x][y]
        canvas[x][y] = '@'
    clean_screen()
    draw_grid(canvas, width)
    inp = getch()

