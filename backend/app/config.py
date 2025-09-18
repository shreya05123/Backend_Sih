import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/plants')
    mqtt_broker: str = os.getenv('MQTT_BROKER', 'mosquitto')
    mqtt_port: int = int(os.getenv('MQTT_PORT', 1883))
    secret_key: str = os.getenv('SECRET_KEY', 'devsecret')

settings = Settings()
