#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    netuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    netuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return netuple
