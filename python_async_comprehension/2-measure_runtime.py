#!/usr/bin/env python3
"""
Import async_generator from the previous task
and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers
using an async comprehension over async_generator,
then return the 10 random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Function async_comprehension that will collect 10 random numbers
    using an async comprehension over async_generator,
    then return the 10 random numbers.

    :param None: None
    Returns:
        List[float]: 10 random numbers - may be float
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
