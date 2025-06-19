import asyncio
from proxybroker import Broker

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print(f"Found proxy: {proxy}")

async def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    await asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit=10),
        show(proxies),
    )

if __name__ == "__main__":
    asyncio.run(main())
