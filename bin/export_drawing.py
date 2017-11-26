from os.path import exists
import re 
from compress import compress

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
        s+= '\n'
    outfile.write("def draw_%s():\n    %s\n\n" % (name, compress(s)))
    outfile.close()
    print("Done!")
