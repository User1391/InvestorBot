from alpha_vantage.timeseries import TimeSeries
import ta

def getData(ticker):
    ts = TimeSeries(key='UFQL6BJD00VWBLZB',output_format='pandas', indexing_type='integer')
    data, metadata = ts.get_daily(ticker)
    # Remember, ^^data^^ is now a Pandas series with our daily data
    highs = data['2. high']
    length = int(highs.size)
    lows = data['3. low']
    closes = data['4. close']
    return highs, lows, closes, length

def indicationADX(ticker):
    high, low, close, len = getData(ticker)
    indicator = ta.trend.ADXIndicator(high, low, close, len)
    return indicator

print(indicationADX('MSFT').adx_pos())
