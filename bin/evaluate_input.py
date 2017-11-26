from base_functions import *
from export_drawing import *

def evaluate_input(inp, x,y, mode,height, width,canvas,brushes, brush_cursor, prev):
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
        if mode == 'WRITE':
            mode = 'MOVE'
        else:
            mode = 'WRITE'
    #eraser mode
    elif inp == 'n':
        if mode != 'ERASE':
            mode = 'ERASE'
        else:
            mode = 'MOVE'
    #clean canvas
    elif inp == 'h':
        clean_grid(canvas, height, width )
        mode = 'MOVE'
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
    if mode == 'WRITE':
        canvas[y][x] = brushes[brush_cursor]
    elif mode == 'MOVE':
        prev = canvas[y][x]
        canvas[y][x] = '@'
    elif mode == 'ERASE':
        canvas[y][x] = '%'

    return (x,y,mode,canvas,brush_cursor, prev)
