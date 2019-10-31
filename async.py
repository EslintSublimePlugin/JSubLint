import asyncio

@asyncio.coroutine
def yield_based_async():
    """Generator-based routine, """
    yield from awaitfn()

async def awaitfun():
    """Native coroutine , latest syntax"""
    await things_to_be_done()
