from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from .database import Base

class Plant(Base):
    __tablename__ = "plants"
    id = Column(String, primary_key=True)
    species = Column(String)

class RiskScore(Base):
    __tablename__ = "risk_scores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(String, ForeignKey("plants.id"))
    ts = Column(DateTime)
    risk_score = Column(Float)
    model_version = Column(String)
    reasons = Column(JSON)
