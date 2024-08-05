#!/usr/bin/python3
'''Task0 module.
'''
import asyncio
import random
import time


def wait_random(max_delay):
    '''Wait a random time and return it.
    '''
    s = time.perf_counter()
    await asyncio.sleep(max_delay)
    run_time = time.perf_counter() - s
    return run_time
