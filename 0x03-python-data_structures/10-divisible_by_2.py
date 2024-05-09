#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mod = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            mod.append(True)
        else:
            mod.append(False)
    return (mod)
