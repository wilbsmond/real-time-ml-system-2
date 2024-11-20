from typing import List
from loguru import logger
from quixstreams import Application

from src.kraken_websocket_api import KrakenWebsockerAPI, Trade

def produce_trades(
    kafka_broker_address: str, 
    kafka_topic: str, 
    product_id: str
):
    """
    Reads trades from the Kraken Websocket API and saves them in the given `kafka_topic`
    
    Args:
        kafka_broker_address (str): The address of the Kafka broker
        kafka_topic (str): The Kafka topic to save the trades
        product_id (str): The product id to get the trades from

    Returns:
        None
    """

    # Create an Application instance with Kafka configs
    app = Application(broker_address=kafka_broker_address)

    # Define a topic "my_topic" with JSON serialization
    topic = app.topic(name=kafka_topic, value_serializer='json')

    # Create a KrakenWebsocketAPI instance
    kraken_api = KrakenWebsockerAPI(product_id=product_id)
    
    # Create a Producer instance
    with app.get_producer() as producer:

        while True:
            trades: List[Trade] = kraken_api.get_trades()

            for trade in trades:
                # Serialize an event using the defined Topic
                # Transform it into a sequence of bytes
                message = topic.serialize(key=trade.product_id, value=trade.model_dump())
                
                # Produce a message into the Kafka topic
                producer.produce(topic=topic.name, value=message.value, key=message.key)

                logger.debug(f"Pushed trade to Kafka: {trade}")

if __name__ == "__main__":
    produce_trades(
        kafka_broker_address='localhost:19092',
        kafka_topic='trade',
        product_id='ETH/EUR',
    )