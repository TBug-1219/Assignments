def readFile():
    numFile = open("randomNumbers.txt", 'r')

    print("Here are the numbers from the file: ")
    for line in numFile:
        numbers = float(line)
        print(numbers)

def getTotal(readFile):
    total = 0.0
    for line in numfile:
        numbers = float(line)
        total += numbers

def getCount(readFile):
    count = 0
    for line in numFile:
        numbers = float(line)
        count += 1

def displayResults(total, count):
    print(f"The total of the numbers is: {total}")
    print(f"The number of numbers is: {count}")
    
def main():
    file = readFile()
    total = getTotal()
    num = getCount()
    results = displayResults()

if __name__ == "__main__":
    main()
