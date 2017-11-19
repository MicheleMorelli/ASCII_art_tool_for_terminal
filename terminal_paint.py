from getch_class import *
from os.path import exists
import re
from sys import exit

def clean_screen():
    print("\n"*120)

def draw_grid(grid,width):
    print('_' * (width+2))
    for row in grid:
        print('|',end = '')
        print(*row,'|', sep = '')
    print('|' * (width + 2))
    print("COMMANDS:\nm - move/write mode\th - clean screen\t[ and ] - change brush\nn - delete mode\t o - export drawing\nq - exit")

def clean_grid(grid):
    for y in range(height):
        for x in range(width):
            grid[y][x] = ' '
        
def draw_brushes(brushes, width, brush_cursor):
    brush_selector = [' ' for i in range(width)]
    brush_selector[brush_cursor] = '^'
    print("BRUSHES:")
    print(*brushes)
    print(*brush_selector)

def export_drawing(grid):
    target_file = './my_ASCII_drawings_functions.py'
    if exists(target_file):
        print("The file %s exists." % target_file)
        q = input("Do you want to save this drawing?(Y/N)")
        
        if re.match('^[Yy]',q):
            outfile = open(target_file , "a")
        else:
            input("No problemo at all! Next time!\n")
            return
    else:
        q = input("the file %s does not exist. Do you want to create it? (Y/N)" % target_file)
        if re.match('^[Yy]', q):
            outfile = open(target_file, 'w+')
            outfile.write("#Created with the Terminal ASCII Paint app by Michele Morelli - https://github.com/MicheleMorelli\n\n")
            outfile = open(target_file, 'a')
        else:
            input('No worries - maybe next time!')
            return
    
    name = input("Name of the drawing?: ")
    s = ''
    for row in grid:
        for i in row:
            #test to fix issue with backslash
            if i == '\\':
                i = '\\\\'
            s += i 
        s+= '\\n'
    outfile.write("def draw_%s():\n    print(\"%s\")\n\n" % (name, s))
    outfile.close()
    print("Done!")

width = 64
height = 16

canvas = [[' ' for i in range(width)] for k in range(height)]
brushes = ['#','*','^','~','0','/','\\','=', '|', '-','_','$','¬','+','(',')' ]
x = 0
y = 0
mode = 'move'
inp = 'g'
prev = ' '
brush_cursor = 0

while inp != 'q':
    if mode == 'move':
        canvas[y][x] = prev
    elif mode == 'delete':
        canvas[y][x] = ' '
    #evaluate input    
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
    elif inp == 'h':
        clean_grid(canvas)
        mode = 'move'
    elif inp == '[' and brush_cursor > 0:
        brush_cursor -= 1
    elif inp == ']' and brush_cursor < len(brushes) - 1:
        brush_cursor += 1
    elif inp == 'o':
        export_drawing(canvas)

    #apply results depending on the mode
    if mode == 'write':
        canvas[y][x] = brushes[brush_cursor]
    elif mode == 'move':
        prev = canvas[y][x]
        canvas[y][x] = '@'
    elif mode == 'delete':
        canvas[y][x] = '%'
    #draw
    clean_screen()
    draw_brushes(brushes,(len(brushes)), brush_cursor)
    draw_grid(canvas, width)

    inp = getch()
