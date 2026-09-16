import os
import time
import asyncio

from capmonstercloudclient.requests import HuntCustomTaskRequest, ProxyInfo
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(hunt_request) for _ in range(num_requests)]


async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(hunt_request))
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    proxy = ProxyInfo(
        proxyType="http",
        proxyAddress="8.8.8.8",
        proxyPort=8080,
        proxyLogin="proxyLoginHere",
        proxyPassword="proxyPasswordHere"
    )
    metadata = {
        "apiGetLib": "https://example.com/hd-api/external/apps/a2157wab1045d68672a63557e0n2a77edbfd15ea/api.js",
    }
    hunt_request = HuntCustomTaskRequest(
        websiteUrl='https://example.com',
        metadata=metadata,
        proxy=proxy,
        userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    )

    nums = 3
    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums))
    print(f'average execution time sync {1/((time.time()-sync_start)/nums):0.2f} ' \
          f'resp/sec\nsolution: {sync_responses[0]}')

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums))
    print(f'average execution time async {1/((time.time()-async_start)/nums):0.2f} ' \
          f'resp/sec\nsolution: {async_responses[0]}')
