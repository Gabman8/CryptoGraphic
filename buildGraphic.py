import pandas as pd
import matplotlib.pyplot as plt
import fetchAPI

def load_graphic(currency, days):
    _, prices = fetchAPI.fetch_historic_data(currency, days)  # No necesitamos timestamps
    media_movil = simple_moving_average(prices, window=days)

    # Crear eje X como números de días
    x = list(range(1, len(prices)+1))

    plt.figure(figsize=(10,5))
    plt.plot(x, prices, label="Precio")
    plt.plot(x, media_movil, label=f"Media Móvil ({days} días)")
    plt.xlabel("Días desde el inicio")
    plt.ylabel("Precio USD")
    plt.title(f"Tendencia del precio de {currency}")
    plt.legend()
    plt.show()
def simple_moving_average(prices, window):
    if len(prices) < window:
        return []
    ma = []
    for i in range(len(prices)):
        if i < window - 1:
            ma.append(None)  # No hay suficiente data
        else:
            ma.append(sum(prices[i-window+1:i+1]) / window)
    return ma
