#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        apex = my_list[0]
        for an in range(len(my_list)):
            if my_list[an] > apex:
                apex = my_list[an]
        return apex
