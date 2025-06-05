#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(2)
    print("Two")

async def count2():
    print("One2")
    await asyncio.sleep(1)
    print("Two2")

async def main():
    await asyncio.gather(count(), count(), count2())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")