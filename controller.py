from timeseries import Timeseries
from pandas import datetime
from pandas import read_csv


tm = Timeseries()

def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

class Controller:
    """
    Module which provides Atelier DB access.
    It contains knowledge of the DB schema and maps higher level
    domain models into DB structures that match the DB schema.
    """

    def __init__(self):
        print "Create controller!!!!!"

    def predict(self):
        print "do staff inside "
        series = read_csv('sample.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
        return tm.predict(series)
