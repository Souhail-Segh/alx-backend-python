#!/usr/bin/python3
'''Task0 module.
'''
import asyncio
import random
import time


async def wait_random(max_delay=10):
    '''Wait a random time and return it.
    '''
    run_time = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return run_time
