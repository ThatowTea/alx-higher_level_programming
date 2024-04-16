#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by ALX School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for ran in range(4, 6):
            c = add(c, ran)
        return (c)
    else:
        return(sub(a, b))
