def flood_fill(canvas,x, y, width, height, brushes, brush_cursor):
    
    initial_x, initial_y = x , y
    while y < height:
        horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x)
        y+=1
    y = initial_y
    while y >= 0:
        horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x)
        y-=1

def horizontal_line(canvas,x, y, width, height, brushes, brush_cursor, initial_x):    
        #horizontal line
        while x < width:
            canvas[y][x] = brushes[brush_cursor]
            x += 1
        x = initial_x
        while x >= 0:
            canvas[y][x] = brushes[brush_cursor]
            x -= 1



