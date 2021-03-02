from pandas import read_csv
from mlflow import pyfunc
import  mlflow

class Controller:

    def __init__(self):
        print( "Create controller!!!!!")
        #self.pyfunc_model = pyfunc.load_model('model')


    def predict(self,data):
        print ("do staff inside .......")
        ## oups that is a steal!!!
        self.pyfunc_model.predict(data)
