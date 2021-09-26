from pycoingecko import CoinGeckoAPI
# open API
qk = CoinGeckoAPI()

cd = qk.get_coins_markets(vs_currency='eur')
