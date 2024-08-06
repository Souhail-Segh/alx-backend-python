#!/usr/bin/env python3
'''Wait randomaly n time.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Wait randomaly between 0 to max_delay for n time.
    '''
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    res_sorted = sorted(res)
    return res_sorted
