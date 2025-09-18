from fastapi import WebSocket

async def farm_ws(websocket: WebSocket, farm_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f'ECHO: {data}')
    except Exception:
        await websocket.close()
