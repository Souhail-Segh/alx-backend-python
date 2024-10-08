#!/usr/bin/env python3
'''Task 4 module.
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''mport async_comprehension from the previous file
    and write a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    '''
    start = time.time()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
        )
    return time.time() - start
