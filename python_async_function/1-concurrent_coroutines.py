#!/usr/bin/env python3
"""
Python - Async
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Simultaneous coroutines with async
    lowest delay returns first to sort the list"""
    random_delays: List[float] = []
    sorted_delays: List[float] = []

    for _ in range(n):
        random_delays.append(wait_random(max_delay))

    for task in asyncio.as_completed(random_delays):
        earliest_result = await task
        sorted_delays.append(earliest_result)

    return sorted_delays
