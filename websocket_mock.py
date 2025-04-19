import asyncio
import csv
import datetime
import ssl

import websockets

#Paremeters of the internal clock
INITIAL_DATE = datetime.datetime.strptime('2025-01-01', '%Y-%m-%d')
DELTA_TIME_SECONDS = 1

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

clock = datetime.datetime.now()

data = []
connections = []
def load_data(path): # If the amount of data is large, consider using a buffer or a similar approach
    global data 
    with open(path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append((datetime.datetime.fromisoformat(row['timestamp']),row['value']))
    data.sort()
    return data

async def simulate_clock(initial_date, delta_seconds):
    global clock
    clock = initial_date
    delta = datetime.timedelta(seconds=delta_seconds)
    while True:
        clock += delta
        print([f"ID: {id(ws)}, Address: {ws.remote_address}" for ws in connections])
        await asyncio.sleep(1)

async def broadcast(message):
    if connections:
        try:
            await asyncio.gather(*(client.send(message) for client in connections))
        except Exception as e:
            print(e)

async def sender():
        i = 0
        while True:
            if i == len(data):
                print('No more data')
                break
            if clock >= data[i][0]:
                message = str(data[i])
                await broadcast(message)
                i += 1
            await asyncio.sleep(1)

async def handle_connection(ws, path = None):

    print(f"Client {ws} connected")

    async def receiver():
        async for message in ws:
            print(f"Recieved: {message}") 
            await ws.send(f"Echo: {message}")

    try:
        connections.append(ws)
        await receiver()
    except websockets.exceptions.ConnectionClosed:
        print('Client desconnected')
    finally:
        if ws in connections:
            connections.remove(ws) 

async def main():
    load_data('random_data.csv')
    asyncio.create_task(simulate_clock(INITIAL_DATE, DELTA_TIME_SECONDS))
    asyncio.create_task(sender())  
    async with websockets.serve(
        handle_connection,
        "localhost", 8765,
        ssl = ssl_context):
        print("Safe WebSocket listening in wss://localhost:8765")
        await asyncio.Future()
      

if __name__ == "__main__":
    asyncio.run(main())