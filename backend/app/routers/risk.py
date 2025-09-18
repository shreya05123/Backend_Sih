from fastapi import APIRouter
from ..schemas import RiskScore
from datetime import datetime

router = APIRouter()

@router.get('/risk/{plant_id}')
def get_risk(plant_id: str):
    return {'plant_id': plant_id, 'risk_score': 0.12, 'ts': datetime.utcnow().isoformat()}
