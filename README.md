## Session 1 todos

- [x] Redpanda up and running
- [x] Push some fake data to Redpanda
- [x] Push real-time (real data) from Kraken Websocket API

## Session 2

- [x] Extract config parameters
- [x] Dockerize it
- [ ] Homework -> adjust the code so that instead of a single product_id, the trade_producer produces data for several product_ids = ['BTC/USD', 'BTC/EUR']
        Ideas: You will need to update
            * the config types
            * the Kraken Websocket API class
- [x] Trade to ohlc service