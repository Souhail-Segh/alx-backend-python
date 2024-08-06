#!/usr/bin/env python3
'''Task0 module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Wait a random time and return it.
    '''
    run_time = random.uniform(max_delay)
    await asyncio.sleep(run_time)
    return run_time
