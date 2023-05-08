"""
Application class has many responsibilities:
        - connect to exchange
        - getting data
        - determine what you should buy or sell?
        - process what the trading bot should do
and according to the SOLID approach, we must avoid creating classes
has many different responsibilities.


To reach this goal:
    - we use template pattern for each of teh step in process
        we standardize process but the steps are different
in tradingbot, the process is same,
    -check price
    -check should buy or sell
    ...
but, the strategy for buying or selling may be different
"""
from typing import List
from abc import ABC, abstractmethod


class TradingBot(ABC):
    """
    the trading bot class contain the main methods of the application instead of explicitly
    implementing like should_buy and should_sell methods, want to make them abstract.
    So we can create sub-classes that perform a particular version of steps we like to have.
    """
    def connect(self, ):
        print(f"connect to crypto exchange ....")

    def get_market_data(self, coint: str) -> List[float]:
        return [10, 12, 18, 14]

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

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


class AverageTrader(TradingBot):

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)

application = AverageTrader()
application.check_price("BTC/USD")
