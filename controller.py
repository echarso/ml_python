from timeseries import Timeseries
from pandas import datetime
from pandas import read_csv
from mlflow import pyfunc
import  mlflow

def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

class Controller:

    def __init__(self):
        print( "Create controller!!!!!")
        self.pyfunc_model = pyfunc.load_model('model')


    def predict(self):
        print ("do staff inside ")
        ## oups that is a steal!!!
        self.pyfunc_model.predict(pd.DataFrame(self.data))
        
