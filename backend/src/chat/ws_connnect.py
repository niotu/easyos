import aiohttp
import asyncio
import time


async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        url = f'http://localhost:8000/chat/ws/{client_id}'
        async with session.get(url) as response:
            text = await response.text()
            with open("http_response.txt", "w") as file:
                file.write(text)


asyncio.run(main())
