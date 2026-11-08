#Name: Victoria Buckner
#Class Section: CS 120 01
#Assignment: Chapter 02 Assignment A
#Program Discription: This program will take a purchase amout and
#calculate the state tax, county tax, total tax, and total purchase amount.

purchaseAmount = float(input("Enter the amount of purchase $"))

taxState = purchaseAmount*0.05

taxCounty = purchaseAmount*0.025

taxTotal = taxState + taxCounty

totalPurchase = purchaseAmount + taxTotal

print("The amount of purchase is: $",purchaseAmount)
print("The state sales tax is: $",taxState)
print("The county sales tax is: $",taxCounty)
print("The total sales tax is: $",taxTotal)
print("The total of the sale is: $",totalPurchase)
