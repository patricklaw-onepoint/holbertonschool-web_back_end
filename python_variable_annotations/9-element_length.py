#!/usr/bin/env python3
"""
Python - Variable Annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return tuple of sequence/int"""
    return [(i, len(i)) for i in lst]
