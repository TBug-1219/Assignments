# Victoria Buckner
# CS120-01
# Programing Assignment 02, Chapter 02
# This program will take the imputed Celsius Temperature and convert it to Fehrenheit.

celsiusTemp = float(input("Enter the Celsius Temperature:"))

multiplicationValue = 9/5

additionValue = 32

celsiusMultiplied = multiplicationValue*celsiusTemp

fahrenheitTemp = celsiusMultiplied + additionValue

print("The fahrenheit temperature converted from celsius is:", fahrenheitTemp)
