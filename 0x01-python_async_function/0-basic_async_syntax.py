#!/usr/bin/env python3
"""basics of asynchronous code"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine"""
    delayed_val = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_val)

    return delayed_val
