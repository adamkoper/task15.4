import pandas as pd
import matplotlib.pyplot as plt

prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25),
]

df = pd.DataFrame(prices, columns=["month", "prices"])
df = df.set_index("month")

prices_PLN = list(map(lambda tup: tup[1], prices))
prices_USD = []

for price_PLN in prices_PLN:
    prices_USD.append(price_PLN/4)


df['price_USD'] = prices_USD

df['price_USD'].plot(kind='line', linewidth=5, linestyle="--", xlim=[0, 12], ylim=[0, 2],
                     colormap='flag', title="Price of goods (USD)").grid()


