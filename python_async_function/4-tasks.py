#!/usr/bin/env python3
"""
Take the code from wait_n
and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called.
"""
import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function task_wait_n that takes in 2 int arguments

    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): max delay to wait_random

    Returns:
        List[float]: list of all delays in ascending order may be float values
    """
    if n <= 0:
        return []

    delay_list = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay_list.append(await task)

    return delay_list
