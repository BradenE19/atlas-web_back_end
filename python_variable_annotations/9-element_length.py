#!/usr/bin/env python3
"""method returns a list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list with type-annotated"""
    return [(i, len(i)) for i in lst]
