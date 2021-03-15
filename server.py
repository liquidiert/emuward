from xdo import Xdo
import keyboard
import asyncio
import websockets

xdo = Xdo()

async def handle_messages(websocket, path):
    async for message in websocket:
        xdo.activate_window(w_id)
        keyboard.press(message)


if __name__=="__main__":

    w_id = xdo.search_windows(b"a7800")
    if len(w_id) > 1:
        raise RuntimeError("Only one emulator window should exist!")
    w_id = w_id[0]
    
    start_server = websockets.serve(handle_messages, "localhost", 5387)
    
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()