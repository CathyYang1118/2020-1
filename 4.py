import websockets
import asyncio

cs = set()

async def talk(websocket,path):
    try:
        while True:
            if (not websocket in cs):
                cs.add(websocket)
                msg = 'welcome:'+str(websocket.remove_address)
            else:
                msg = str(websocket.remote_address)+'says:'+str(await websocket.recv())
            await asyncio.wait([ws.send(msg) for ws in cs])
    except Exception as err:
        cs.remove(websocket)

start_server = websockets.serve(talk,'192.168.123.187',8764)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
