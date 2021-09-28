
import datetime
import time
#time1=datetime.datetime.now()
#print(type(time1))



'''string_time1="{}".format(time1)
#print(type(time1))
print(string_time1)
print(string_time1[0])
spliced= string_time1[10:19]
print(spliced)
hour=string_time1[10:13]
print(hour)
min=string_time1[14:16]
print(min)
'''

isTracking = False


def first_scan():
  global isTracking
  if isTracking == False:
    startingTime=datetime.datetime.now()
    startingTime="{}".format(startingTime)
    global startingHour1
    global startingMin1
    isTracking=True 
    startingHour1= startingTime[10:13]
    startingMin1 = startingTime[14:16]
    startingHour1=int(startingHour1)-6
    if startingHour1<=0:
      startingHour1=startingHour1+24
    startingMin1=int(startingMin1)
    return startingHour1
    return startingMin1
    return isTracking
  else:
    second_scan()



def second_scan():
  startingTime=datetime.datetime.now()
  startingTime="{}".format(startingTime)
  global startingHour2
  global startingMin2
  startingHour2= startingTime[10:13]
  startingMin2 = startingTime[14:16]
  startingHour2=int(startingHour2)-6
  if startingHour2<=0:
    startingHour2=startingHour2+24
  startingMin2=int(startingMin2)
  isTracking=False
  return startingHour2
  return startingMin2


def total_time():
  global totalHours
  global totalMin
  totalHours=startingHour2-startingHour1
  totalMin=startingMin2-startingMin1
  if totalHours>=2:
    totalHours=2
  return totalHours
  return totalMin

first_scan()
second_scan()
total_time()