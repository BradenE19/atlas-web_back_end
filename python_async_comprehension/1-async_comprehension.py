#!/usr/bin/env python3
"""coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers."""
import asyncio
from typing import List
async_ = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers."""
    random_numbers = [i async for i in async_()]
    return random_numbers