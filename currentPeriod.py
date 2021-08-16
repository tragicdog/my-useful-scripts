####################################################
# Title: Current Period
# Author: Jonathon Lillie
# Version: 1
# Description: Using the start times for the periods it compares the current day/time to the start times and tells the user which period it currently is, and if no periods are found true it outputs that school is not in session
####################################################
import datetime
currentDate = datetime.datetime.now()
#print(currentDate.strftime('%A - %X'))

# Tues-Fri Start Times
p1tfStart = '08:30'
p2tfStart = '09:33' 
p3tfStart = '10:41'
p4tfStart = '11:44' 
p5tfStart = '13:17' 
p6tfStart = '14:20' 
p6tfEnd = '15:15' 

# Monday start times
p1mStart = '08:30'
p2mStart = '09:26' 
p3mStart = '10:22'
p4mStart = '11:23' 
p5mStart = '12:49'
p6mStart = '13:45'
p6mEnd = '14:33'

# Minimum day start times
p1mmStart = '08:30'
p2mmStart = '09:14'
p3mmStart = '09:58'
p4mmStart = '10:42'
p5mmStart = '11:26'
p6mmStart = '12:10'
p6mmEnd = '12:46'

# Rally day start times
p1rStart = '08:30'
p2rStart = '09:24' 
p3rStart = '10:22'
p4rStart = '11:16' 
p5rStart = '13:40' 
p6rStart = '14:34' 
p6rEnd = '15:20' 

# Block Days (should be an array)
#TODO make array that is parsed using the Block Days
#blockDays =  datetime.datetime.strptime('September, 2','%B,%d')

# Minimum days (should be an array)
#TODO make array that is parsed using the minimum days

# Rally days (should be an array)
#TODO make array that is parsed using the Rally days


#current date/time
now = datetime.datetime.now()
currentTime = now.strftime('%H:%M')

weekno = datetime.datetime.today().weekday()
print("---------------------------------------------")
if weekno < 5:
    print("It's a Weekday: ", now.strftime('%A %H:%M'))
    if  weekno == 0:
      if currentTime >  p1mStart and currentTime < p2mStart:
        print("It's currently 1st period")
      elif currentTime >  p2mStart and currentTime < p3mStart:
        print("It's currently 2nd Period")
      elif currentTime >  p3mStart and currentTime < p4mStart:
        print("It's currently 3rd Period")
      elif currentTime >  p4mStart and currentTime < p5mStart:
        print("It's currently 4th Period")
      elif currentTime >  p5mStart and currentTime < p6mStart:
        print("It's currently 5th Period")
      elif currentTime >=  p6mStart and currentTime <= p6mEnd:
        print("It's currently 6th Period")
      elif currentTime >= p1mStart and currentTime <= p6mEnd:
        print("It's currently a passing period")
      else:
        print("School is not in session!")
    else:
      print("it's not Monday")
      if currentTime >=  p1tfStart and currentTime <= p2tfStart:
        print("It's currently 1st period")
      elif currentTime >=  p2tfStart and currentTime <= p3tfStart:
        print("It's currently 2nd Period")
      elif currentTime >=  p3tfStart and currentTime <= p4tfStart:
        print("It's currently 3rd Period")
      elif currentTime >=  p4tfStart and currentTime <= p5tfStart:
        print("It's currently 4th Period")
      elif currentTime >=  p5tfStart and currentTime <= p6tfStart:
        print("It's currently 5th Period")
      elif currentTime >=  p6tfStart and currentTime <= p6tfEnd:
        print("It's currently 6th Period")
      elif currentTime >= p1tfStart and currentTime <= p6tfEnd:
        print("It's currently a passing period")
      else:
        print("School is not in session!")
else:  # 5 Sat, 6 Sun
    print("It's the weekend, school is not in session!!!")
print("---------------------------------------------")

