#Victoria Buckner
#CS 120 01
#Assignment 02, Chapter 06
#This program will use the file made with
#the last assignment. It will read the numbers
#on that file and display all of the numbers
#thhe total of the numbers and the number of
#random numbers it read from the file.

def main():
    numFile = open("randomNumbers.txt", 'r')
    total = 0.0
    count = 0

    print("Here are the numbers from the file: ")
    for line in numFile:
        numbers = float(line)
        count += 1
        print("#", count, ": ", numbers, sep="")
        total += numbers
        
    numFile.close()
    print(f"The total of the numbers is: {total}")
    print(f"The number of numbers is: {count}")

if __name__ == "__main__":
    main()
