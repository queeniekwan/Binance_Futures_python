from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=DKnzx80rRN3f7TTHcGbcOHUWj5RLIgkky2ta4Po3D10xOI9wzbjyQ3Ot817aRaqG, secret_key=CfNtVN2VjfMQju5FJOdPP8vQwglUMomQYet8CaCwth4zz9tElUyTDgxRjD8gPKO5)

result = request_client.get_ticker_price_change_statistics()
# result = request_client.get_ticker_price_change_statistics(symbol="BTCUSDT")

print("======= 24hr Ticker Price Change Statistics =======")
PrintMix.print_data(result)
print("===================================================")
