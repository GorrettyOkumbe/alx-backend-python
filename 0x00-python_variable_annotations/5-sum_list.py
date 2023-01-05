#!/usr/bin/env python3
"""Annotates collections like a list"""


def sum_list(input_list: list[float]) -> float:
    """
    sum_list: takes a list of floating point numbers
    input_list - the list of floats
    Returns:
        sum of the elements of a list as afloat
    """
    sum = 0.0
    for i in input_list:
        sum += i
    return float(sum)
