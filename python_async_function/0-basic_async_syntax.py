#!/usr/bin/env python3
"""
0. The basics of async

Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.

Use the random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function wait_random:
    takes in an integer argument
    waits for a random delay between
    0 and max_delay (included and float value)
    seconds and eventually returns it.

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        float: the return value is the random number may be float
    """
    # generate random delay between 0 and max_delay
    random_delay = random.uniform(0, max_delay)

    # sleep for the random delay asynchronously
    await asyncio.sleep(random_delay)

    return random_delay
