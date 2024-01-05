#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    def multiplier(n: float) -> float:
        """returns a function that multiplies a float by multiplier."""
        return n * multiplier
    return multiplier
