#Victoria Buckner
#CS 120 01
#Chapter 08 Assignment A
#This program will ask the user to input a string of single
#digit numbers then separate them into integers and add
#them together. Finally, it will display the results.

def main():
    numberString = input("Enter a string of single digit numbers"\
                        "(with nothing separating them): ")
    totalSum = 0

    for ch in numberString:
        totalSum += int(ch)

    print("The sum of the numbers is:", (totalSum))

main()
