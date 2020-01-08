#Daniel Pingrey
#1/20
#Vacation Planner

import datetime
import math
import random

#tuple of activities and their costs
options = ("Snorkeling","Scuba Diving","Fishing","Sunbathing","Shopping","Helicopter Ride","Sleeping")
prices  = (10.00, 150.00, 25.00, 0.00, 200.00, 450.00, 0.00)

#Gets and converts starting date
startDateString = input("\nEnter the date you would like to start your vacation (MM/DD/YYYY): ")
startDate = datetime.datetime.strptime(startDateString, "%m/%d/%Y")

#Gets and converts ending date
stopDateString = input("Enter the date you plan on heading home and ending your vacation (MM/DD/YYYY): ")
stopDate = datetime.datetime.strptime(stopDateString, "%m/%d/%Y")

#Calculates how many days the vacation will be
delta = stopDate - startDate
print(str.format("\nYour vacation is {} days long.\n", delta.days))

costs = []

#Will print what you could do each day of your vacation and how much it costs
for i in range(0, delta.days):
    
    activityIndex = random.randrange(0, len(options))
    activity = options[activityIndex]
    cost = prices[activityIndex]

    thisDate = startDate + datetime.timedelta(days = i)
    
    thisDateString = thisDate.strftime("%m/%d/%Y")
    
    print(str.format("On {}, {} costs ${:.2f}",thisDateString,activity,cost))
    costs.append(cost)

#Tells the stats of the vacation
print(str.format("\nThe most expensive day cost ${:.2f}\n", max(costs)))
print(str.format("The least expensive day cost ${:.2f}\n", min(costs)))
print(str.format("The total cost of your trip was ${:.2f}\n", sum(costs)))
print(str.format("The average amount spent on your trip is ${:.2f}\n", sum(costs)/len(costs)))



