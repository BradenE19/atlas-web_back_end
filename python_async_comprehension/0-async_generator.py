#!/usr/bin/env python3

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:

    for i in range(10):
        # wait asynchronously for 1 second
        await asyncio.sleep(1)
        # yield a random number between 0 and 10
        yield random.uniform(0, 10)