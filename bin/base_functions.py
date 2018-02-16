'''
This module contains the base functions for the ASCII art tool.
'''

def clean_screen():
    '''
    Cleans the screen.
    
    Returns:
        None
    '''
    print("\n"*120)

def draw_grid(grid,width, mode):
    '''
    Draws the canvas, based on the values of the 2d-list 'grid'.

    Arguments:
        grid    aka the canvas aka 2d list 
        width   width of the canvas
        mode    current mode (e.g. "WRITE", or "MOVE")

    Returns:
        None
    '''
    mode_str = mode + " MODE"
    number_of_spaces = width - len('COMMANDS:') - len(mode_str)
    print('_' * (width+2))
    for row in grid:
        
        # FIX01: Fixed unpacker issue with older versions of Python 
        print('|',end = '') 
        for i in row:
            print (i, end='')
        print("|")
        # FIX01 END ----------------------------------------------

    print('|' * (width + 2)) 
    print("COMMANDS:"+" " * number_of_spaces + mode_str + "\nm - move/write mode\th - clean screen\t[ and ] - change brush\nn - delete mode \to - export drawing\tj - paint bucket\nq - exit")

def clean_grid(grid, height, width):
    '''
    Sets all the values of the canvas (aka the grid) to " ".

    Arguments:
        grid    aka the canvas aka 2d list 
        heigth  heigth of the canvas
        width   width of the canvas

    Returns:
        None
    '''
    for y in range(height):
        for x in range(width):
            grid[y][x] = ' ' 
            
def draw_brushes(brushes, width, brush_cursor):
    '''
    This function draws the brushes based on the list defined in terminal_paint.

    Arguments:
        brushes     list of characters, that are used as ASCII 'brushes' 
        width       width of the canvas
        brush_cursor int, indicating the current index of the brushes list 

    Returns:
        None
    '''
    brush_selector = [' ' for i in range(width)]
    brush_selector[brush_cursor] = '^' 
    print("BRUSHES:")
    print(*brushes)
    print(*brush_selector)


def flood_fill(canvas,x, y, width, height, brushes, brush_cursor, previous_content):
    '''
    Flood fill function, which uses a simple recursive algorithm.
    TODO: there is a bug that happens when this function is used on a cell that has
    the same brush type as the current.

    Arguments:
        canvas          The canvas, that is, a 2-d list.
        x               Current x position
        y               Current y position
        width           Width of the canvas
        heigth          Heigth of the canvas
        brushes         Brushes 1D list
        brush_cursor    int, indicating the current index of the brushes list
        previous_content previous content of the cell

    Returns:
        None

    '''
    in_the_grid = (x >= 0) and (x < width) and (y >= 0) and (y < height)
    if not in_the_grid or canvas[y][x] != previous_content:
        return
    canvas[y][x] = brushes[brush_cursor]
    flood_fill(canvas,x+1, y, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x-1, y, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x, y+1, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x, y-1, width, height, brushes, brush_cursor, previous_content)

