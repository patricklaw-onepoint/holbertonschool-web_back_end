#!/usr/bin/env python3
"""
Python - Variable Annotations
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple with a squre of v"""
    return (k, v * v)
