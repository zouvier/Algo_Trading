import backtrader
import datetime
from trading_strategies import TestStrategy
brains = backtrader.Cerebro()

brains.broker.set_cash(1000000)

data_feed = backtrader.feeds.YahooFinanceCSVData(
    dataname='oracle_test_data.csv',
    fromdate=datetime.datetime(1996, 1, 1),
    todate=datetime.datetime(2012, 12, 31),
    reverse=False)

brains.adddata(data_feed)
brains.addstrategy(TestStrategy)
brains.addsizer(backtrader.sizers.FixedSize, stake=1000)
print('Starting Portfolio Value: %.2f' % brains.broker.getvalue())

brains.run()

print('Final Portfolio Value: %.2f' % brains.broker.getvalue())

brains.plot()
