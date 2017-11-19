s = "################################################################\n##|^^^^^^|###########|^^^^^^^^^^^^|############|^^^^^^^^^^^|####\n##|______|###########|____________|############|___________|####\n################################################################\n////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////\n ///  ///  ///  ///  ///  ///  ///  ///  ///  ///  ///  ///  ///\n///  ///  ///  ///  ///  ///  ///  ///  ///  ///  ///  ///  /// \n////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////\n================================================================\n________________________________________________________________\n   |     |     |     |     |     |     |     |     |     |     |\n__ |____ |____ |____ |____ |____ |____ |_____|_____|_____|_____|\n|     |      |      |     |     |     |     |     |     |     | \n|_____|______|______|_____|_____|_____|_____|_____|_____|_____|_\n"

s = list(s)
c = dict()
out = 'print("'

while s:
    #with this check I assume that the last char of each of these strings is a \n, so I will add it once out of the loop
    if len(s) == 1:
        break
    i = 0
    #if single character, pushes it straight in the array (adds an extra '\' in case of a special character)
    if s[i] != s[i+1]:
        if s[i] == '\n':
            s[i] = '\\n'
        out = out + s[i] +'"+"'
    # if multiple chars in a row, then counts the instances with a dictionary count, an pushes string with multiplication of number of instances (TODO: fix the ugly +1 workaround)
    else:
        while s[i] == s[i+1]:
            if s[i] in c:
                c[s[i]] +=1
            else:
                c[s[i]] = 1
            i += 1
         # TODO: the one below is the ugly +1 workaround - it does not count the last instance(because the next char is different)
        out =  out + s[i] + '"*' +  str(c[s[i]] + 1) + '+"'
        i = c[s[i]] # i becomes the number of instances of the char (it stays one if it's only one instance)
        c[s[i]] = 0

    del s[0:i + 1] #again, the ugly +1 workaround

print(out + '\\n")')
