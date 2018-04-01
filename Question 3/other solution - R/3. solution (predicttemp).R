# utility function
predictTemperature <- function(data, startDate, endDate, p, n) {
  #strt<- paste(startDate,"00:00")
  strt<-startDate
  s<-as.numeric(as.POSIXlt(strt,format="%Y-%m-%d",tz="UTC"))
  
  old<-s
  x<-c()
  for(counter in 1:24*p){
    x[counter]<-old
    old<-old+3600
  }    
  y <-data
  print(startDate)
  print(y)
  
  linear <-lm(y~x)
  print(summary(linear)) 
  
  e<-as.numeric(as.POSIXlt(endDate,format="%Y-%m-%d",tz="UTC"))
  
  f<-e
  z<-c()
  for(counter in 1:24*n){
    z[counter]<-f
    f<-f+3600
  }
  r <- data.frame(x=z)
  
  i<-predict(linear,r) 
  return(i)
}

# dummy inputs (one day)
data<-c(10.0,11.1,12.3,13.2,14.8,15.6,16.7,17.5,18.9,19.7,20.7,21.1,22.6,23.5,24.9,25.1,26.3,27.8,28.8,29.6,30.2,31.6,32.1,33.7)
startDate <- '2013-01-01'
endDate <- '2013-01-01'
p<-1
n<-1

# call the utility function
answer <- predictTemperature(data, startDate, endDate, p, n)
answer