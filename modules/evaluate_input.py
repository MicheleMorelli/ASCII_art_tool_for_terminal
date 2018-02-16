from base_functions import *
from export_drawing import *

def evaluate_input(inp, x,y, mode,height, width,canvas,brushes, brush_cursor, prev):
    '''
    Takes the user's input as an argument and modifies the canvas 2d list based
    on the value of 'mode' and the current brush.

    Arguments:
        inp             the user's input - i.e. a char
        x               x of current location
        y               y of current location
        mode            current mode 
        height          heigth of the canvas
        width           width of the canvas
        canvas          a 2d list
        brushes         the list of brushes
        brush_cursor    the index of the current brush
        prev            the previous value

    Returns:
        (x,y,mode,canvas,brush_cursor, prev)

    '''
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
        # BUG002 fix - checking that the current brush is not the same as
        # current symbol.
        if canvas[y][x] != brushes[brush_cursor]:
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
