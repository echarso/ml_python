from pandas import read_csv
from mlflow import pyfunc
import numpy as np
import pandas as pd

class Controller:

    def __init__(self):
        print( "Create controller!!!!!")
        f = open("conf.txt", "r")
        conf = f.read()
        conf = conf.split(',\n')
        self.name = conf[0]
        self.version = conf[1]
        self.source = conf[2]
        print(self.name, ' ',self.version, ' ',self.source )
        self.pyfunc_model = pyfunc.load_model('model')
        f.close()

    def predict(self,data):
        print ("do staff inside .......")
        print (data)
        print (type(data))
        print( "****************************9999")
        input = pd.DataFrame(columns=data['columns'],data= np.array(data['data']))
        print(input)
        ret={}
        ret['predictions'] =  self.pyfunc_model.predict(input)
        ret['name']=self.name
        ret['version']=self.version
        ret['source']=self.source
        print( "----------predict done -----------------")

        print(ret)
        print( "----------predict done -----------------")

        return ret
