from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

#https://people.duke.edu/~rnau/411arim.htm
# https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
class Timeseries:
    """
    Module which provides Atelier DB access.
    It contains knowledge of the DB schema and maps higher level
    domain models into DB structures that match the DB schema.
    """

    def __init__(self):
        print "Create timeseries!!!!!"
    def parser(x):
    	return datetime.strptime('190'+x, '%Y-%m')
    def predict(self, series ):
        X = series.values
        size = int(len(X) * 0.66)
        train, test = X[0:size], X[size:len(X)]
        history = [x for x in train]
        predictions = list()
        for t in range(len(test)):
        	model = ARIMA(history, order=(5,1,0))
        	model_fit = model.fit(disp=0)
        	output = model_fit.forecast()
        	yhat = output[0]
        	predictions.append(yhat)
        	obs = test[t]
        	history.append(obs)
        	print('predicted=%f, expected=%f' % (yhat, obs))
        error = mean_squared_error(test, predictions)
        print('Test MSE: %.3f' % error)
        return predictions