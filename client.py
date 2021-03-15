import keyboard
import websockets
import asyncio

async def send_keys():
    uri = "ws://localhost:5387"
    async with websockets.connect(uri) as websocket:
        while True:
            key = keyboard.read_key()
            await websocket.send(key)

if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(send_keys())
