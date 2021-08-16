####################################################
# Title: Current Period
# Author: Jonathon Lillie
# Version: 1
# Description: Using the start times for the periods it compares the current day/time to the start times and tells the user which period it currently is, and if no periods are found true it outputs that school is not in session
####################################################

import datetime
currentDate = datetime.datetime.now()
#print(currentDate.strftime('%A - %X'))

# Monday start times
p1mStart = '08:30'
p1mEnd = '09:18'
p2mStart = '09:26'
p2mEnd = '10:14' 
p3mStart = '10:22'
p3mEnd = '11:15'
p4mStart = '11:23'
p4mEnd = '12:11' 
p5mStart = '12:49'
p5mEnd = '13:37'
p6mStart = '13:45'
p6mEnd = '14:33'
mLunchStart = '12:11'
mLunchEnd = '12:41'

# Tues-Fri Start Times
p1tfStart = '08:30'
p1tfEnd = '09:25'
p2tfStart = '09:33' 
p2tfEnd = '10:33'
p3tfStart = '10:41'
p3tfEnd = '11:36'
p4tfStart = '11:44' 
p4tfEnd = '12:39'
p5tfStart = '13:17' 
p5tfEnd = '14:12'
p6tfStart = '14:20' 
p6tfEnd = '15:15' 
tfLunchStart = '12:39'
tfLunchEnd = '13:09'

# Minimum day start times
p1mmStart = '08:30'
p1mmEnd = '09:06'
p2mmStart = '09:14'
p2mmEnd = '09:50'
p3mmStart = '09:58'
p3mmEnd = '10:34'
p4mmStart = '10:42'
p4mmEnd = '11:18'
p5mmStart = '11:26'
p5mmEnd = '12:02'
p6mmStart = '12:10'
p6mmEnd = '12:46'
mmLunchStart = '12:46'
mmLunchEnd = '13:21'

# Rally day start times
p1rStart = '08:30'
p1rEnd = '08:30'
p2rStart = '09:24'
p2rEnd = '10:14' 
p3rStart = '10:22'
p3rEnd = '11:08'
p4rStart = '11:16' 
p4rEnd = '12:02'
p5rStart = '13:40'
p5rEnd = '14:24' 
p6rStart = '14:34' 
p6rEnd = '15:20'
rallyStart = '12:02'
rallyEnd = '13:02' 
rLunchStart = '13:02'
rLunchEnd = '13:32'

# Block Days (should be an array)
#TODO make array that is parsed using the Block Days 9/2, 9/3, 10/21, 10/22, 3/10, 3/11, 5/19, 5/20
#blockDays =  datetime.datetime.strptime('September, 2','%B,%d')

# Minimum days (should be an array) 
# 9/9 Back to School Night
# 9/24 Homecomming
# 6/9 Last day of school
#TODO make array that is parsed using the minimum days

# Rally days (should be an array)
#TODO make array that is parsed using the Rally days
# 9/24, 1/28, 4/22

#current date/time
now = datetime.datetime.now()
currentTime = now.strftime('%H:%M')

weekno = datetime.datetime.today().weekday()
print("---------------------------------------------")
if weekno < 5:
    print("It's a Weekday: ", now.strftime('%A %H:%M'))
    if  weekno == 0: #mon = 0, tues = 1, weds = 2, thurs = 3, fri = 4
      if currentTime >  p1mStart and currentTime <= p1mEnd:
        print("It's currently 1st period")
      elif currentTime >  p2mStart and currentTime <= p2mEnd:
        print("It's currently 2nd Period")
      elif currentTime >  p3mStart and currentTime <= p3mEnd:
        print("It's currently 3rd Period")
      elif currentTime >  p4mStart and currentTime <= p4mEnd:
        print("It's currently 4th Period")
      elif currentTime >  p5mStart and currentTime <= p5mEnd:
        print("It's currently 5th Period")
      elif currentTime >=  p6mStart and currentTime <= p6mEnd:
        print("It's currently 6th Period")
      elif currentTime >= mLunchStart and currentTime <= mLunchEnd:
        print("It's currently lunch")
      elif currentTime >= p1mStart and currentTime <= p6mEnd:
        print("It's currently a passing period")
      else:
        print("School is not in session!")
    else: #mon = 0, tues = 1, weds = 2, thurs = 3, fri = 4
      print("it's not Monday")
      if currentTime >=  p1tfStart and currentTime <= p1tfEnd:
        print("It's currently 1st period")
      elif currentTime >=  p2tfStart and currentTime <= p2tfEnd:
        print("It's currently 2nd Period")
      elif currentTime >=  p3tfStart and currentTime <= p3tfEnd:
        print("It's currently 3rd Period")
      elif currentTime >=  p4tfStart and currentTime <= p4tfEnd:
        print("It's currently 4th Period")
      elif currentTime >=  p5tfStart and currentTime <= p5tfEnd:
        print("It's currently 5th Period")
      elif currentTime >=  p6tfStart and currentTime <= p6tfEnd:
        print("It's currently 6th Period")
      elif currentTime >= tfLunchStart and currentTime <= tfLunchEnd:
        print("It's currently lunch")
      elif currentTime >= p1tfStart and currentTime <= p6tfEnd:
        print("It's currently a passing period")
      else:
        print("School is not in session!")
else:  # Sat = 5, Sun = 6
    print("It's the weekend, school is not in session!!!")
print("---------------------------------------------")
