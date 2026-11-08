#Victoria Buckner
#CS 120 01
#Assignment01,Chapter04
#This program asks the user for a string of
#numbers until the user ends the string with
#-99 then it will determine the lowest and
#greatest number.

print("Enter a number or enter -99 to end.")

number = int(input("Enter a number:"))

lowest = number
greatest = number

while (number := int(input("Enter a number:")))!= -99:
    if number < lowest:
        lowest = number
    elif number > greatest:
        greatest = number
    

print("The lowest number is:", lowest)
print("The greatest number is:", greatest)
