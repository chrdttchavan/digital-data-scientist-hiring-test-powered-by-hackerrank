# necessary import libraries
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

# utility function
def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    x = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in knownTimestamps]
    y = humidity

    lm = LinearRegression()
    lm.fit(np.array(x).reshape(-1,1),y)

    z = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in timestamps]
    return lm.predict(np.array(z).reshape(-1,1))

# dummy inputs
startDate = '2013-01-01'
endDate = '2013-01-01'
knownTimestamps = ['2013-01-01 07:00', '2013-01-01 08:00', '2013-01-01 09:00', '2013-01-01 10:00',
                      '2013-01-01 11:00', '2013-01-01 12:00']
humidity = [10.0, 11.1, 13.2, 14.8, 15.6, 16.7]
timestamps= ['2013-01-01 13:00', '2013-01-01 14:00']

# call the utility function
answer = predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps)
print(answer)