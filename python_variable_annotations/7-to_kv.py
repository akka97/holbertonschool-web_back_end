#!/usr/bin/env python3
"""documentation"""


from typing import List, Union, Tuple


def to_ktv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """from element to tuple"""
    sec_element = v ** 2
    return (k, sec_element)
    
