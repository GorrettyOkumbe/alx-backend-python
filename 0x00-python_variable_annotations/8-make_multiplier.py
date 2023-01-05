#!/usr/bin/env python3

"""multiplies float numbers"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplication of  float numbers"""

    return lambda x: x * multiplier
