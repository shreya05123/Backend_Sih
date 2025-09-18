from fastapi import FastAPI
from routers import plants, farms, risk, actuators
import ws, mqtt_client

app = FastAPI(title="Extended Hybrid Backend")

app.include_router(plants.router, prefix="/api/v1")
app.include_router(farms.router, prefix="/api/v1")
app.include_router(risk.router, prefix="/api/v1")
app.include_router(actuators.router, prefix="/api/v1")

app.add_api_websocket_route("/ws/farm/{farm_id}", ws.farm_ws)

@app.on_event("startup")
async def startup_event():
    mqtt_client.start_mqtt()

@app.get("/")
def root():
    return {"status": "backend running"}
