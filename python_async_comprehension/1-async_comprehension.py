#!/usr/bin/env python3
'''async file'''
import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''async generator'''
    return [element for element in async_generator()]
