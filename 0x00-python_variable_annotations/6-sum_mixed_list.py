#!/usr/bin/env python3
"""module of a mixed list containing floats and integers"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates sum of list elements of both float and int types"""
    return float(sum(mxd_lst))
