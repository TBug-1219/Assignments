# Victoria Buckner
# CS 120 01
# Assignment 02, Chapter 04
# This program will show the increase in
# an $8,000 tuition by 3% each year for
# the next 5 years

tuitionIncrease = 0.03
years = 5
tuition = int(input("Enter tuition:"))

print("The projected tuition for the next 5 years is:")
for year in range(1, years + 1):
    increase = (tuition * tuitionIncrease)
    total = (tuition + increase)
    tuition = total
    print(f"Year {year}: ${total:.2f}")

    
    
