def clean_screen():
    print("\n"*120)

def draw_grid(grid,width, mode):
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
    for y in range(height):
        for x in range(width):
            grid[y][x] = ' ' 
            
def draw_brushes(brushes, width, brush_cursor):
    brush_selector = [' ' for i in range(width)]
    brush_selector[brush_cursor] = '^' 
    print("BRUSHES:")
    print(*brushes)
    print(*brush_selector)


def flood_fill(canvas,x, y, width, height, brushes, brush_cursor, previous_content):
    in_the_grid = (x >= 0) and (x < width) and (y >= 0) and (y < height)
    if not in_the_grid or canvas[y][x] != previous_content:
        return
    canvas[y][x] = brushes[brush_cursor]
    flood_fill(canvas,x+1, y, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x-1, y, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x, y+1, width, height, brushes, brush_cursor, previous_content)
    flood_fill(canvas,x, y-1, width, height, brushes, brush_cursor, previous_content)
