import asyncio
import websockets
import json

BTC_USD = "BTC-USD"
ETH_USD = "ETH-USD"
ETH_BTC = "ETH-BTC"
TRADES = ["BTC-USD", "ETH-USD", "ETH-BTC"]
DATA_FEEDS = []


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


async def stream(msg, url):
    async with websockets.connect(url) as ws:
        await ws.send(msg)
        while True:
            try:
                response = await ws.recv()
                result = json.loads(response)
                if "type" in result.keys() and result['type'] == "ticker":
                    if len(DATA_FEEDS) == 200:
                        DATA_FEEDS.pop(0)
                    price = (float(result['open_24h']) + float(result['high_24h']) + float(result['low_24h'])) / 3
                    DATA_FEEDS.append({
                        "product_id": result['product_id'],
                        "price": price,
                        "volume": float(result['volume_24h']),
                    })
                    calculate_vwap(DATA_FEEDS)
                await asyncio.sleep(3)
            except Exception as e:
                print(e)
                await ws.close()
                break

if __name__ == "__main__":
    url = "wss://ws-feed.pro.coinbase.com"
    params = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": TRADES}]
    }
    loop = asyncio.get_event_loop()
    loop.run_until_complete(stream(json.dumps(params), url))
