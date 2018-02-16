import zlib

def compress(s):
    '''
    This function takes a string and converts it into a Python-compatible
    string to be used in a print statement. This may come handy for 
    very long strings with many repetitions.

    Example:
        converts
        "aaaa    bbbb ccc\n"
        to
        "a"*4 + " "*4 + "b"*4 +" " + "c"*3 + "\n"

    Arguments:
        s a string

    Returns:
        a string in the ([any substring*] * n...) to be used with a print statement 
        in a Python script.

    '''
    s = list(s)
    c = dict()
    out = 'print("'

    while s:
        #with this check I assume that the last char of each of these strings is a \n, so I will add it once out of the loop
        if len(s) == 1:
            break
        i = 0
        #if single character, pushes it straight in the array (adds an extra '\' in case of a special character / backlash)
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
    # NOT REALLY NEEDED, so I commented it out;
    #compress with zlib
    #comp = zlib.compress((out + '\\n")').encode("ascii") ) TODO
    #print(comp)
    return out + '\\n")'
