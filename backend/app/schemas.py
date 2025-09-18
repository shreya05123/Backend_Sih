from pydantic import BaseModel
import datetime
from typing import Optional

class Telemetry(BaseModel):
    plant_id: str
    ts: Optional[datetime.datetime] = None
    voc: Optional[dict] = None
    thermal: Optional[dict] = None
    cv_meta: Optional[dict] = None
    biochemical: Optional[dict] = None

class RiskScore(BaseModel):
    plant_id: str
    ts: datetime.datetime
    risk_score: float
    model_version: str
    reasons: Optional[dict] = None
