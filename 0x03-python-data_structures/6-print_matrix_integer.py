#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rows in range(len(matrix)):
            for i in range(len(matrix[rows])):
                if i != len(matrix[rows]) - 1:
                    ends = ' '
                else:
                    ends = ''
                print("{:d}".format(matrix[rows][i]), end=ends)
            print()


