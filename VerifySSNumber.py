#Daniel Pingrey
#1/20
#Verifying Social Security

for i in range(0,3):
    SSnumber = int(input("Please enter you social security number: "))


    if (SSnumber >= 10000000) and (SSnumber <= 1000000000):
        print("\nNumber validated:", SSnumber)
        break
    else:
        print("\nInvalid number\n")

print("\nProgram ended. Thank you for your cooperation =]")
