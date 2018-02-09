# ASCII Art tool for the terminal #
## By Michele Morelli - 2017 ##
![vimrc](https://github.com/MicheleMorelli/terminal_paint/blob/master/doc/pics/example.png)

This simple program allows to draw cool ASCII art in the command line quickly and easily, and to export it to use it in order to make your Python programs look beter in the terminal.

As for the commands, I was inspired heavily by Vim. 
You move the cursor by using the wasd buttons, and can move/draw/erase depending on the mode you are in.

There is currently a fairly limited amount of brushes and tools, but I wanted to focus on the stability of the core idea first, and then expand the options once the core application is solid enough. 

At the moment all the 'brushes' are simple ASCII glyphs. I want to expand it to include some crazy UTF-8, but again, I prefer to keep everything simple at the beginning, and then add more features later.

Among the other things, I am planning to add the possibility to export the drawings in different formats, and as strings for different languages.

## How to use the ASCII Art command line tool ##

Please note that this code has only been tested on Linux for now, so I am not sure whether it would work as expected in a Windows environment.

You will need to have Python3 installed to use this tool.

To use it:
- Clone this repo somewhere your machine;
- You can run it with:
 $./ASCII_Art_Tool

Alternatively, you can call:
 $python3 bin/terminal_paint.py

(The latter method has chances to work also on Windows). 

Have fun! :-)
