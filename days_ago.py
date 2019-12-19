"""promblem solved for the Talk Python course
https://github.com/talkpython/100daysofcode-with-python-course"""

import datetime
from datetime import date, timedelta

print("This program allows you to enter a date to find out how many days ago it occurred")

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: ")) 
date_entered = date(year, month, day)
now = date.today()
days = (now - date_entered).days     
print("The date",date_entered, "was", days, "ago.")
      


