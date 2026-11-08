#Victoria Buckner
#CS 120 01
#Assignment 01, Chapter 06
#This program Takes the number numbers the user
#wants to imput to a file and writes them to said
#file. The number of numbers is in the range of
#1-500. 

import random

def genRandNum(numFile, count):
    with open(numFile, 'w') as file:
        for _ in range(count):
            randomNumber = random.randint(1, 500)
            file.write(f"{randomNumber}\n")
    print(f"{count} random numbers have been written to {numFile}.")

def main():
    try:
        count = int(input("Enter the amount of numbers to generate: "))
        if count < 1:
            print("Enter a number greater than 1")
            return
    except ValueError:
        print("Invalid input. Enter a valid integer.")
        return

    numFile = "randomNumbers.txt"
    genRandNum(numFile, count)

if __name__ == "__main__":
    main()
