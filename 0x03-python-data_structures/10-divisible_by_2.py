#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    second_list = []
    if my_list:
        for number in my_list:
            second_list.append(False if number % 2 else True)
        return second_list
