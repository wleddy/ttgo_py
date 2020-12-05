#asyncio url fetch exmaple
try:
    import asyncio
except ImportError:
    import uasyncio as asyncio
try:
    import requests
except ImportError:
    import urequests as requests

import time
try:
    import open_wallace
except ImportError:
    pass

async def download_site(url):
    response = reqeusts.get(url)
    print("Read {0} from {1}".format(response.content_length, url))

async def download_all_sites(sites):
    tasks = []
    for url in sites:
        task = asyncio.ensure_future(download_site(url))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print("Downloaded {size} in {duration} seconds".format(size=len(sites),duration=duration))
    