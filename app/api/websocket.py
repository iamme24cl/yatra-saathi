from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from uuid import UUID
from app.core.redis import redis_client 
import json 

router = APIRouter()

@router.websocket("/ws/track_driver/{driver_id}")
async def track_driver(websocket: WebSocket, driver_id: UUID):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            channel = f"driver:{driver_id}"
            await redis_client.publish(channel, json.dumps(data))
    except WebSocketDisconnect:
        print(f"Driver {driver_id} disconnected")
      
@router.websocket("/ws/booking_updates/{booking_id}/{driver_id}")
async def booking_updates(websocket: WebSocket, booking_id: UUID, driver_id: UUID):
    await websocket.accept()
    
    driver_channel = f"driver:{driver_id}"
    booking_channel = f"booking:{booking_id}"
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(driver_channel, booking_channel)
    
    try: 
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"])
    except WebSocketDisconnect:
        print(f"User disconnected from booking {booking_id}")
        await pubsub.unsubscribe(driver_channel, booking_channel)