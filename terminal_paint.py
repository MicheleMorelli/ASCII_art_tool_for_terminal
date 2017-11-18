from getch_class import *

def clean_screen():
    print("\n"*120)

def draw_grid(grid,width):
    print('_' * (width+2))
    for row in grid:
        print('|',end = '')
        print(*row,'|', sep = '')
    print('|' * (width + 2))
    print('COMMANDS:\nm\tmove/write modes\nn\tdelete mode\nq\texit')

width = 64
height = 16

canvas = [[' ' for i in range(width)] for k in range(height)]
x = 0
y = 0
mode = 'move'
inp = 'g'
prev = ' '
while inp != 'q':
    if mode == 'move':
        canvas[y][x] = prev
    elif mode == 'delete':
        canvas[y][x] = ' '
        
    if inp == 'a' and x > 0:
        x -= 1
    elif inp == 'd' and x < width -1:
        x += 1
    elif inp == 'w' and y > 0:
        y -= 1
    elif inp == 's' and y < height - 1:
        y += 1
    elif inp == 'm':
        if mode == 'write':
            mode = 'move'
        else:
            mode = 'write'
    elif inp == 'n':
        if mode != 'delete':
            mode = 'delete'
        else:
            mode = 'move'
    if mode == 'write':
        canvas[y][x] = '#'
    elif mode == 'move':
        prev = canvas[y][x]
        canvas[y][x] = '@'
    elif mode == 'delete':
        canvas[y][x] = '%'
    clean_screen()
    draw_grid(canvas, width)
    inp = getch()

