# necessary import libraries
import numpy as np
import datetime,time
from sklearn.linear_model import LinearRegression

# dummy inputs
startDate = '2013-01-01'
endDate = '2013-01-01'
knownTimestamps = ['2013-01-01 07:00','2013-01-01 08:00','2013-01-01 09:00','2013-01-01 10:00','2013-01-01 11:00','2013-01-01 12:00']
humidity = [10.0,11.1,13.2,14.8,15.6,16.7]
# note the extra first element here
timestamps = ['x','2013-01-01 13:00','2013-01-01 14:00']

# utility function
def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    x = []
    for i in range(len(knownTimestamps)):
        x.append(time.mktime(datetime.datetime.strptime(knownTimestamps[i],"%Y-%d-%m %H:%M").timetuple()))
    y = humidity
    lm = LinearRegression()
    lm.fit(np.asarray(x).reshape(-1,1),y)
    z = []
    for i in range(1,len(timestamps)):
        z.append(time.mktime(datetime.datetime.strptime(timestamps[i],"%Y-%d-%m %H:%M").timetuple()))
    return(lm.predict(np.asarray(z).reshape(-1,1)).tolist())

# call the utility function
print(predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps))