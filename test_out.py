from os.path import exists
import re
from sys import exit

target_file = './my_ASCII_drawings_functions.py'
if exists(target_file):
    print("The file %s exists." % target_file)
    outfile = open(target_file , "a")
else:
    q = input("the file %s does not exist. Do you want to create it? (Y/N)" % target_file)
    if re.match('^[Yy]', q):
        outfile = open(target_file, 'w+')
        outfile.write("#Created with the Terminal ASCII Paint app by Michele Morelli - https://github.com/MicheleMorelli\n\n")
        outfile = open(target_file, 'a')
    else:
        input('Goodbye!')
        exit()


for i in range(10):
    name = input("Name of the function?: ")
    outfile.write("def draw_%s():\n    print('test')\n\n" % name)
outfile.close()
print("Done!")
