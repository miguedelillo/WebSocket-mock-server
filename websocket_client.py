import asyncio
import ssl

import websockets

ssl_context = ssl._create_unverified_context() # Ignores the self-signed certificate

async def test():
    uri = 'wss://localhost:8765'
    try:
        async with websockets.connect(uri, ssl=ssl_context) as ws:
            print('Connected succesfully')

            await ws.send('Hi')
            print('Message sent')
            while True:
                res = await ws.recv()
                print(f'Response: \n {res}')
    except Exception as e:
        print(f'Unexcepcted error: {e}')

asyncio.run(test())