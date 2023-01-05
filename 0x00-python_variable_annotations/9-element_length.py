#!/usr/bin/env python3
"""Duck typing"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """computes the length of a list and tuple"""

    return [(i, len(i)) for i in lst]
