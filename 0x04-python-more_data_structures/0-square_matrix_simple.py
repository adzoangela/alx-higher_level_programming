#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_values = []
    for each_line in matrix:
        squared_values.append([a**2 for a in each_line])
    return squared_values
