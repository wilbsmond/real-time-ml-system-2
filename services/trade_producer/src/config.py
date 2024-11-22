from pydantic_settings import BaseSettings
from pydantic import Field

class AppConfig(BaseSettings):
    kafka_broker_address: str = Field(env="KAFKA_BROKER_ADDRESS")
    kafka_topic: str = Field(env="KAFKA_TOPIC")
    product_id: str = Field(env="PRODUCT_ID")

    class Config:
        env_file = ".env"

config = AppConfig()