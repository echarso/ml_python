from timeseries import Timeseries
from pandas import datetime
from pandas import read_csv


tm = Timeseries()

def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

class Controller:
    
    def __init__(self):
        print "Create controller!!!!!"

    def predict(self):
        print "do staff inside "
        ## oups that is a steal!!!
        series = read_csv('sample.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
        return tm.predict(series)
