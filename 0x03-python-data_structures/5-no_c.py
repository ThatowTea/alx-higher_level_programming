#!/usr/bin/python3
def no_c(my_string):
    lin = len(my_string)
    fint = 0
    nstr = my_string[:]
    for i in range(lin):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            nstr = nstr[:(i - fint)] + my_string[(i + 1):]
            fint += 1
    return (nstr)
