from xdo import Xdo
import keyboard
import asyncio
import websockets
import argparse

xdo = Xdo()

async def handle_messages(websocket, path):
    async for message in websocket:
        xdo.activate_window(w_id)
        keyboard.press(message)

def get_args():
    parser = argparse.ArgumentParser(description="emuward - A simple key forwarder")
    parser.add_argument("--ip", type=str, nargs=1, default="localhost", help="Ip to use")
    parser.add_argument("--port", type=int, nargs=1, default=5387, help="Which port to use")
    parser.add_argument("--appname", type=str, nargs=1, required=True, help="Name of the application xdotool should target")
    return parser.parse_args()

if __name__=="__main__":

    args = get_args()

    w_id = xdo.search_windows(args.appname.encode())
    if len(w_id) > 1:
        raise RuntimeError("Only one emulator window should exist!")
    w_id = w_id[0]

    start_server = websockets.serve(handle_messages, args.ip, args.port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
