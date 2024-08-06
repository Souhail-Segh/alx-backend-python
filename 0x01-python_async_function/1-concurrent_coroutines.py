#!/usr/bin/env python3
'''Wait randomaly n time.
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay: int = 10):
    '''Wait randomaly between 0 to max_delay for n time.
    '''
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    res_sorted = sorted(list(res))
    return res_sorted
