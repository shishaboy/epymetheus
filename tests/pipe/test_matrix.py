# import pytest  # noqa

# import numpy as np
# import pandas as pd

# from epymetheus import Universe, Trade, TradeStrategy
# from epymetheus.pipe.matrix import (
#     _lot_matrix,
#     _value_matrix,
# )


# # TODO this is just tentative; add multiple and robust tests


# def make_universe(n_bars, n_assets, pricedata=None):
#     if pricedata is None:
#         pricedata = np.zeros((n_bars, n_assets))
#     prices = pd.DataFrame(
#         pricedata,
#         index=[f'Bar{i}' for i in range(n_bars)],
#         columns=[f'Asset{i}' for i in range(n_assets)],
#     )
#     return Universe(prices)


# class MockStrategy(TradeStrategy):
#     def logic(self, universe):
#         pass


# def make_strategy(universe=None, trades=None):
#     strategy = MockStrategy()
#     if universe:
#         strategy.universe = universe
#     if trades:
#         strategy.trades = trades
#     return strategy


# # --------------------------------------------------------------------------------


# def test_lot_matrix():
#     universe = make_universe(100, 3)
#     trades = [
#         Trade(asset=['Asset0', 'Asset1'], lot=[1, -2], open_bar='Bar0'),
#         Trade(asset=['Asset2', 'Asset1'], lot=[3, 4], open_bar='Bar0'),
#     ]
#     strategy = make_strategy(universe=universe, trades=trades)

#     lot_expected = np.array([
#         [1, 0],
#         [-2, 4],
#         [0, 3],
#     ])

#     assert np.equal(_lot_matrix(strategy), lot_expected).all()


# def test_value_matrix():
#     pricedata = np.array([
#         [1, 10, 100],
#         [2, 20, 200],
#         [3, 30, 300],
#         [4, 40, 400],
#     ])
#     universe = make_universe(4, 3, pricedata)
#     trades = [
#         Trade(asset=['Asset0', 'Asset1'], lot=[1, -2], open_bar='Bar0'),
#         Trade(asset=['Asset2', 'Asset1'], lot=[3, 4], open_bar='Bar0'),
#     ]
#     strategy = make_strategy(universe=universe, trades=trades)

#     value_expected = np.array([
#         [-19, 340],
#         [-38, 680],
#         [-57, 1020],
#         [-76, 1360],
#     ])

#     assert np.equal(_value_matrix(strategy), value_expected).all()
