from websocket import create_connection
import json
import time

BTC_USD = "BTC-USD"
ETH_USD = "ETH-USD"
ETH_BTC = "ETH-BTC"
TRADES = ["BTC-USD", "ETH-USD", "ETH-BTC"]


def calculate_vwap(feeds_data):
    trades = {
        BTC_USD: {
            "total_price_volume": 0,
            "total_volume": 0
        },
        ETH_USD: {
            "total_price_volume": 0,
            "total_volume": 0
        },
        ETH_BTC: {
            "total_price_volume": 0,
            "total_volume": 0
        }
    }

    for data in feeds_data:
        if data['product_id'] == BTC_USD:
            trades[BTC_USD]['total_price_volume'] += data['price'] * data['volume']
            trades[BTC_USD]['total_volume'] += data['volume']
        elif data['product_id'] == ETH_USD:
            trades[ETH_USD]['total_price_volume'] += data['price'] * data['volume']
            trades[ETH_USD]['total_volume'] += data['volume']
        elif data['product_id'] == ETH_BTC:
            trades[ETH_BTC]['total_price_volume'] += data['price'] * data['volume']
            trades[ETH_BTC]['total_volume'] += data['volume']
    if trades[BTC_USD]['total_volume'] > 0:
        print(f"{BTC_USD} Volume Weighted Average Price is {trades[BTC_USD]['total_price_volume']/trades[BTC_USD]['total_volume']}")
    if trades[ETH_USD]['total_volume'] > 0:
        print(f"{ETH_USD} Volume Weighted Average Price is {trades[ETH_USD]['total_price_volume']/trades[ETH_USD]['total_volume']}")
    if trades[ETH_BTC]['total_volume'] > 0:
        print(f"{ETH_BTC} Volume Weighted Average Price is {trades[ETH_BTC]['total_price_volume']/trades[ETH_BTC]['total_volume']}")


if __name__ == '__main__':
    # URL = "wss://ws-feed-public.sandbox.pro.coinbase.com"
    URL = "wss://ws-feed.pro.coinbase.com"
    ws = create_connection(URL)
    params = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD", "ETH-USD", "ETH-BTC"]}]
    }

    data_feeds = []
    while True:
        ws.send(json.dumps(params))
        result = ws.recv()
        time.sleep(1)
        converted = json.loads(result)
        print(converted)
        if "type" in converted.keys() and converted['type'] == "ticker":
            if len(data_feeds) == 200:
                data_feeds.pop(0)
            price = (float(converted['open_24h']) + float(converted['high_24h']) + float(converted['low_24h']))/3
            print(float(converted['price']), price)
            data_feeds.append({
                "product_id": converted['product_id'],
                "price": price,
                "volume": float(converted['volume_24h']),
            })
            calculate_vwap(data_feeds)
