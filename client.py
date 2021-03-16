import keyboard
import websockets
import asyncio

async def send_keys():
    uri = "ws://localhost:5387"
    async with websockets.connect(uri) as websocket:
        while True:
            key = keyboard.read_event()
            await websocket.send(str(key.scan_code))

if __name__=="__main__":
    asyncio.run(send_keys())
