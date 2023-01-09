#!/usr/bin/env python3
"""Synchronous code"""


from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ A synchronous(regular function)"""
    task_1 = create_task(wait_random(max_delay))
    return task_1
