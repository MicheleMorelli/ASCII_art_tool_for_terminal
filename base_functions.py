def clean_screen():
    print("\n"*120)

def draw_grid(grid,width):
    print('_' * (width+2))
    for row in grid:
        print('|',end = '') 
        print(*row,'|', sep = '') 
    print('|' * (width + 2)) 
    print("COMMANDS:\nm - move/write mode\th - clean screen\t[ and ] - change brush\nn - delete mode\t o - export drawing\nq - exit")

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

