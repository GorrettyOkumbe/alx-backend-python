#!/usr/bin/env python3
""" measure run time module """


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time
    Returns:
        total_time/n as float
    """
    starting_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - starting_time) / n
