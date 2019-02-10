#!/usr/bin/env python

# WS server example

import sys
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    greeting = f"Hello {name}!"
    await websocket.send(greeting)

start_server = websockets.serve(hello, 'localhost', 8765)
print('the server runs!')
asyncio.get_event_loop().run_until_complete(start_server)
print('the server is completed!')
asyncio.get_event_loop().run_forever()
print('the server exits!')