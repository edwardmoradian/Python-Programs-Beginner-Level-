# Author:  Edward Moradian

Time = input("Please enter the number of seconds: ")
Time = float(Time)

Hours = 0
Minutes = 0
Seconds = 0

if Time <= 3600:
    Minutes = Time // 60
    Seconds = Time % 60

print("Your time is ",Minutes, " minutes and ",Seconds," seconds")