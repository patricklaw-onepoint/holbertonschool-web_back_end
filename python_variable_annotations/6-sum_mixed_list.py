#!/usr/bin/env python3
"""
Python - Variable Annotations
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of list of int/floats"""
    return sum(mxd_lst)
