#!/usr/bin/env python3
"""
Python - Variable Annotations
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """return a list"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), int(3.0))
