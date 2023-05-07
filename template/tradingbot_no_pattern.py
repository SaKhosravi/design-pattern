"""
In this example, we have a trading robot that is supposed to
receive the price of a currency, then based on a strategy,
it will offer to buy, sell or no-action.
"""
from typing import List


class Application:
    """
    responsibility of this class:
        - connect to exchange
        - getting data
        - determine what you should,buy or sell?
        - process what the tradingbot should do
    """

    trading_strategy: str

    def __init__(self, trading_strategy="average") -> None:
        self.trading_strategy = trading_strategy

    def connect(self,):
        print("connect to crypto exchange ....")

    def get_market_data(self, coint: str) -> List[float]:
        return [10, 12, 18, 14]

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_price(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)

        if should_buy:
            print(f"you should by{coin}")
        elif should_sell:
            print(f"you should sell {coin}")
        else:
            print(f"no action on this {coin}")


application = Application("minmax")
application.check_price("BTC/USD")
