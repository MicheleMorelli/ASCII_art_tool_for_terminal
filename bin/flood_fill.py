def flood_fill(canvas,x, y, width, height, brushes, brush_cursor):
    
    initial_x, initial_y = x , y
    while y < height and canvas[y][x] != brushes[brush_cursor] :
        horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x)
        y+=1
    y = initial_y
    while y >= 0 and canvas[y-1][x] != brushes[brush_cursor]:
        horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x)
        y-=1

def horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x):    
        #horizontal line
        while x < width and canvas[y][x] != brushes[brush_cursor]:
            canvas[y][x] = brushes[brush_cursor]
            x += 1
        x = initial_x
        while x >= 0 and canvas[y][x-1] != brushes[brush_cursor]:
            canvas[y][x] = brushes[brush_cursor]
            x -= 1



