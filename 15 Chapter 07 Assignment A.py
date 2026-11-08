#Victoria Buckner
#CS 120 01
#Assignment 01, Chapter 07
#This program will let the user input
#the total rainfall for each of the 12
#months into an array. Then it will
#calculate and display the total rainfall
#for the year, the average monthly rainfall,
#and the highest and lowest amounts.

MONTHS = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

def getRainfallData():
    rainfall = []
    for month in MONTHS:
        amount = float(input(f"Enter the total rainfall for {month}: "))
        while amount < 0:
            print("Error, please enter a non-negative number.")
            amount = float(input(f"Enter the total rainfall "\
                                 "for {month}: "))
            continue
        rainfall.append(amount)
    return rainfall


def getTotalRainfall(rainfall):
    return sum(rainfall)

def getAverageRainfall(rainfall):
    return sum(rainfall)/len(rainfall)

def getHighestLowestRainfall(rainfall):
    maxRainfall  = max(rainfall)
    minRainfall = min(rainfall)
    maxMonth = MONTHS[rainfall.index(maxRainfall)]
    minMonth = MONTHS[rainfall.index(minRainfall)]
    return maxRainfall, minRainfall, maxMonth, minMonth

def main():
    rainfall = getRainfallData()
    totalRainfall = getTotalRainfall(rainfall)
    averageRainfall= getAverageRainfall(rainfall)
    maxRainfall, minRainfall, maxMonth, minMonth = getHighestLowestRainfall(rainfall)

    print(f"Total rainfall for the year: {totalRainfall}")
    print(f"Average monthly rainfall: {averageRainfall}")
    print(f"Month with the highest rainfall: {maxMonth}({maxRainfall})")
    print(f"Month with lowest rainfall: {minMonth}({minRainfall})")

if __name__ == "__main__":
    main()
