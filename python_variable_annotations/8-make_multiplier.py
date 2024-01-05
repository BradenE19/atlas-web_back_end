#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies a float by multiplier.
    """
    def multiplier_function(number: float) -> float:
        """
        Function that multiplies the function argument by
        multiplier argument from the parent function.
        """
        return number * multiplier
    return multiplier_function