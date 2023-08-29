#!/usr/bin/env python3
"""documentation"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length iteration"""
    return [((i, len(i)) for i in lst)]
