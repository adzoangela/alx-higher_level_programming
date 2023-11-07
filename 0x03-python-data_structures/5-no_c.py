#!/usr/bin/python3
def no_c(my_string):
    new_strr = ""
    for elem in my_string:
        if elem != "c" and elem != "C":
            new_strr += elem
    return new_strr
