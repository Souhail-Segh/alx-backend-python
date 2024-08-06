#!/usr/bin/env python3
'''Calculate the average executin time of co-routines.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measure average time of asyncio.sleep.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    return (stop_time - start_time) / n
