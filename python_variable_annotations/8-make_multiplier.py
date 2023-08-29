#!/usr/bin/env python3
"""documentation"""


from typing import Callable, Iterator, Union, Optional


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make callable"""
    def make_multiply(x: float) -> float:
        return (x * multiplier)
    return make_multiply

