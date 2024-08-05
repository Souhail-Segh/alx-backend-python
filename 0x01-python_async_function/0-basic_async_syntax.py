#!/usr/bin/python3
'''Task0 module.
'''
import asyncio
import random
import time


async def wait_random(max_delay=10):
    '''Wait a random time and return it.
    '''
    s = time.perf_counter()
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    run_time = time.perf_counter() - s
    return run_time
