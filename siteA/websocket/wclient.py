#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        name = input("What's your name? ")
        print(f"< {name}")
        await websocket.send(name)        
        greeting = await websocket.recv()
        print(f"> {greeting}")
        
        if name == 'exit':
            return None
        else:
            return name        

while(asyncio.get_event_loop().run_until_complete(hello()) != None):
    pass

print('the client exits!')