#!/usr/bin/env python3

""" complex types string and float to tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes astring and floats converts to  tuple"""

    return (k, v**2)
