import asyncio
import websockets
import json
import main
# create handler for each connection
async def handler(websocket, path):
   data = await websocket.recv()
   dataJson = json.loads(data)
   id = dataJson['id']
   price = dataJson['price']
   qty = dataJson['quantity']
   msg = dataJson['supporter_message']
   reply = f"Qty {qty} dan Msg {msg}!"
   f = open('settings.json')
   data = json.load(f)
   for i in data['settings']:
      if qty >= i['min_qty']:
        if msg in i['allowedCommand']:
            main.runCmd(msg)
   print(reply)
   await websocket.send(reply)

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()