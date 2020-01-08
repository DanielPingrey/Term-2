#Daniel Pingrey
#1/20
#Verification

import datetime

#The get_verified_integer function
def get_verified_integer(prompt, min, max):

    while True:
        try:
            inputString = input(prompt)
            inputInt = int(inputString)

            if (inputInt >= min) and (inputInt <= max):
                return inputInt
            else:
                print("Try again -", end="")
        except:
            print("Try again -", end="")



month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ",2000,2030)


today = datetime.date(year, month, day)
print("Today is a " + today.strftime("%A"))


