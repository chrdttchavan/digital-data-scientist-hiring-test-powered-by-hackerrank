# utility function
predictMissingHumidity <- function(startDate, endDate, knownTimestamps, humidity, timestamps){
  x <- as.numeric(as.POSIXct(knownTimestamps, format="%Y-%m-%d %H:%M"))
  y<- humidity
  
  linear<-lm(y~x)
  # skipping first element of timestamps due to the extra first element
  z <- as.numeric(as.POSIXct(timestamps[2:length(timestamps)], format="%Y-%m-%d %H:%M")) 
  z <- data.frame(x=z)
  
  return(predict(linear,z))
}

# dummy inputs
startDate <- '2013-01-01'
endDate <- '2013-01-01'
knownTimestamps <- c('2013-01-01 07:00','2013-01-01 08:00','2013-01-01 09:00','2013-01-01 10:00','2013-01-01 11:00','2013-01-01 12:00')
humidity<-c(10.0,11.1,13.2,14.8,15.6,16.7)
# note the extra first element here
timestamps <- c('x','2013-01-01 13:00','2013-01-01 14:00')

# call the utility function
answer <- predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps)
answer