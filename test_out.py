from os.path import exists
import re
from sys import exit

target = './target.py'
if exists(target):
    print("The file %s exists." % target)
    outfile = open(target , "a")
else:
    q = input("the file %s does not exist. Do you want to create it? (Y/N)" % target)
    if re.match('^[Yy]', q):
        outfile = open(target, 'w+')
        outfile.write("#Created with the Terminal ASCII Paint app by Michele Morelli - https://github.com/MicheleMorelli\n\n")
        outfile = open(target, 'a')
    else:
        input('Goodbye!')
        exit()


for i in range(10):
    name = input("Name of the function?: ")
    outfile.write("def draw_%s():\n    print('test')\n\n" % name)
outfile.close()
print("Done!")
