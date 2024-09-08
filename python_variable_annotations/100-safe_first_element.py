#!/usr/bin/env python3
"""
Python - Variable Annotations
"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """get first element safely"""
    if lst:
        return lst[0]
    return None
