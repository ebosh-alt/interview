import logging
from fastapi import FastAPI

from services.Coinmarket import CoinMarket

app = FastAPI()


@app.get("/get_coin/{name_coin}")
async def get_coin(name_coin: str):
    logging.info(name_coin)
    coin_market = CoinMarket(name_coin)
    result = await coin_market.get()
    return result


@app.get("/get_name_coins")
async def get_coin():
    return CoinMarket.all_coin
