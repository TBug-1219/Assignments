#Victoria Buckner
#CS 120 01
#Assignment 02, Chapter 03
#This program will ask the user to input the package
#weight and then calculate the shipping rate based
#on the weight of the package.

SHIP1 = 1.50
SHIP2 = 3.00
SHIP3 = 4.00
SHIP4 = 4.75

package_weight = float(input("Enter the package weight:"))

if package_weight > 10:
    PRICE1 = package_weight * SHIP4
    print("The shipping price is $", PRICE1)
elif package_weight > 6:
    PRICE2 = package_weight * SHIP3
    print("The shipping price is $", PRICE2)
elif package_weight > 2:
    PRICE3 = package_weight * SHIP2
    print("The shipping price is $", PRICE3)
elif package_weight > 0:
    PRICE4 = package_weight * SHIP1
    print("The shipping price is $", PRICE4)
else:
    print("Invalid weight, please try again,")
