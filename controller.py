from pandas import read_csv
from mlflow import pyfunc
import  mlflow
import pandas as pd

class Controller:

    def __init__(self):
        print( "Create controller!!!!!")
        self.pyfunc_model = pyfunc.load_model('model')


    def predict(self,data):
        print ("do staff inside .......")
        ## oups that is a steal!!!
        print (data)
        print (type(data))
        print( "****************************9999")

        input = pd.DataFrame(columns=data['columns'],data=data['data'])
        print(input)
        ret =  self.pyfunc_model.predict(input)
        print( "----------predict done -----------------")

        print(ret)
        return ret
