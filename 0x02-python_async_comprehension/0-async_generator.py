#!/usr/bin/env python3
"""Async Generator module"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """asynchronous generator"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
