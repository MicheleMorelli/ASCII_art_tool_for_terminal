from getch_class import *
from evaluate_input import * 
from sys import exit
from base_functions import *
from evaluate_input import * 
from os import get_terminal_size

def terminal_paint():
    '''
    Main loop. 
    TODO - refactoring needed!
    
    Arguments:
        None

    Returns:
        None


    '''

    terminal = get_terminal_size()
    width = terminal.columns - int(terminal.columns * .2)
    height = width // 4
    
    canvas = [[' ' for i in range(width)] for k in range(height)]
    brushes = ['#','*','^','~','0','/','\\','=', '|', '-','_','$','¬','+','(',')','.',':','<','>']
    x = 0
    y = 0
    mode = 'MOVE'
    inp = ' '
    prev = ' '
    brush_cursor = 0

    #main loop
    while inp != 'q':
        if mode == 'MOVE':
            canvas[y][x] = prev
        elif mode == 'ERASE':
            canvas[y][x] = ' '
        #evaluate input and apply changes
        x,y,mode,canvas,brush_cursor, prev = evaluate_input(inp, x,y, mode,height, width,canvas,brushes, brush_cursor, prev)
        #draw everything
        clean_screen()
        draw_brushes(brushes,(len(brushes)), brush_cursor)
        draw_grid(canvas, width,mode)
        #get input
        inp = getch()

    #cleans screen before exiting
    clean_screen()
    print("="*20+"\nGoodbye!\n"+"="*20)
