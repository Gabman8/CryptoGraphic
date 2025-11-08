import requests
import sqlite3
import datetime

# API call to fetch crypto data
def fetch_data(crypto_currency):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": crypto_currency.lower()}
    response = requests.get(url, params=params)
    return response.json()
def fetch_historic_data(crypto_symbol, days):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_symbol.lower()}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Debug: ver qué devuelve la API
    print("DEBUG fetch_historic_data:", data)

    if "prices" not in data:
        raise ValueError(f"No se encontraron datos de precios para {crypto_symbol}")

    timestamps = [datetime.datetime.fromtimestamp(point[0]/1000) for point in data["prices"]]
    prices = [point[1] for point in data["prices"]]

    return timestamps, prices
