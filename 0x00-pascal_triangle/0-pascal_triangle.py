#!/usr/bin/python3
"""
Pascal's triangle
functions:
    - factorial
    - choose(combinatorics)
    - pascal_triangle
"""


def factorial(num):
    """
    calculate the factorial of a number(num)
    """
    if num <= 0:
        return 1
    else:
        return num*factorial(num - 1)


def choose(n, r):
    """
    nCr(n choose r): find how many different combinations of r items
    can be chosen from a set of n items
    """
    return (factorial(n))//(factorial(n-r)*factorial(r))


def pascal_triangle(n):
    """
    create a pascal's triangle of n
    """
    pascal = []
    temp = []
    if n <= 0:
        return pascal
    for i in range(n):
        for j in range(0, i + 1):
            elem = choose(i, j)
            temp.append(elem)
        pascal.append(temp)
        temp = []
    return pascal
