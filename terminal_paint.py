from getch_class import *

def clean_screen():
    print("\n"*120)

def draw_grid(grid):
    for row in grid:
        print(*row, sep = '')




canvas = [[' ' for i in range(32)] for k in range(16)]
cursor = (0,0)

inp = getch()
while inp != 'q':
    if inp == 'a':
    elif inp == 'd':
    elif inp == 'w':
    elif inp == 's':
    clean_screen()
    draw_grid(canvas)
    print('you inputted',inp)
    inp = getch()

