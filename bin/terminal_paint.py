from getch_class import *
from sys import exit
from base_functions import *
from export_drawing import *

width = 64
height = 16

canvas = [[' ' for i in range(width)] for k in range(height)]
brushes = ['#','*','^','~','0','/','\\','=', '|', '-','_','$','¬','+','(',')','.',':','<','>']
x = 0
y = 0
mode = 'move'
inp = ' '
prev = ' '
brush_cursor = 0

while inp != 'q':
    if mode == 'move':
        canvas[y][x] = prev
    elif mode == 'delete':
        canvas[y][x] = ' '
    #evaluate input 
    #left
    if inp == 'a' and x > 0:
        x -= 1
    #right
    elif inp == 'd' and x < width -1:
        x += 1
    #up
    elif inp == 'w' and y > 0:
        y -= 1
    #down
    elif inp == 's' and y < height - 1:
        y += 1
    #move/write mode
    elif inp == 'm':
        if mode == 'write':
            mode = 'move'
        else:
            mode = 'write'
    #eraser mode
    elif inp == 'n':
        if mode != 'delete':
            mode = 'delete'
        else:
            mode = 'move'
    #clean canvas
    elif inp == 'h':
        clean_grid(canvas, height, width )
        mode = 'move'
    #change brush
    elif inp == '[' and brush_cursor > 0:
        brush_cursor -= 1
    elif inp == ']' and brush_cursor < len(brushes) - 1:
        brush_cursor += 1
    #export string
    elif inp == 'o':
        export_drawing(canvas)

    #flood fill
    elif inp == 'j':
        flood_fill(canvas,x,y, width, height, brushes, brush_cursor, canvas[y][x])

    #apply results depending on the mode
    if mode == 'write':
        canvas[y][x] = brushes[brush_cursor]
    elif mode == 'move':
        prev = canvas[y][x]
        canvas[y][x] = '@'
    elif mode == 'delete':
        canvas[y][x] = '%'
    #draw everything
    clean_screen()
    draw_brushes(brushes,(len(brushes)), brush_cursor)
    draw_grid(canvas, width)
    #get input
    inp = getch()
#cleans screen before exiting
clean_screen()
print("="*20+"\nGoodbye!\n"+"="*20)
