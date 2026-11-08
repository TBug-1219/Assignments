#Victoria Buckner
#CS 120 01
#Final Project
#This program will read the phone numbers written
#in the form of 555-GET-HELP and put it through
#code that will convert the letters into the correct
#corresponding number. It will then display the
#number in the original form and the converted
#form next to each other for the user to see clearly.

#This module is setting the letters equal to the
#correct numbers.
def letterToNumber(letter):
    #Setting mapping equal to the letters
    #with their corresponding numbers.
    mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
        }
    #Returning mapping with getting upercase
    #letters and letter.
    return mapping.get(letter.upper(), letter)

#This module is converting the characters or
#letters to the corresponding numbers.
def convertPhoneNumber(phoneNumber):
    #Setting convertedNumber equal to nothing first.
    convertedNumber = ""
    #For each character in phoneNumber do the following.
    for ch in phoneNumber:
        #Set convertedNumber plus/equal to letterToNumber
        #for each character.
        convertedNumber += letterToNumber(ch)
    #Return the variable convertedNumber
    return convertedNumber

#This module is going to read the numbers from the file.
def readNumbersFromFile(fileName):
    #With the open file fileName in the read format
    #as  the file do the following.
    with open(fileName, 'r') as file:
        #Return the line stripped for each line in the file.
        return [line.strip() for line in file]

#This module is going to write the converted numbers to a file.
def writeConvertedNumbersToFile(fileName, originalNumbers,
                                convertedNumbers):
    #With the open file fileName in the write format
    #as the file do the following.
    with open(fileName, 'w') as file:
        #Write to the file: Original Number next to
        #Converted Number.
        file.write("Original Number\tConvertedNumber\n")
        #For the original and converted in the zip file of
        #originalNumbers and convertedNumbers, do the following.
        for original, converted in zip(originalNumbers,
                                       convertedNumbers):
            #Write to the file: original next to converted.
            file.write(f"{original}\t{converted}\n")

#This module is going to set some more variables and call
#the modules.
def main():
    #Set the imputFile variable equal to the original file.
    inputFile = 'wordNumbers.txt'
    
    #Set the outputFile variable equal to the new file.
    outputFile = 'convertedNumbers.txt'
    
    #Set the originalNumbers variable equal to the
    #readNumbersFromFile module.
    originalNumbers = readNumbersFromFile(inputFile)
    
    #Set the convertedNumbers variable equal to the
    #convertPhoneNumber module for each number in originalNumbers.
    convertedNumbers = [convertPhoneNumber(number) for number in originalNumbers]

    #Call the writeConvertedNumbersToFile module.
    writeConvertedNumbersToFile(outputFile, originalNumbers, convertedNumbers)

    #Display Original Number next to Converted Number.
    print("Original Number\tConverted Number")

    #For the original and the converted inthe zip file of
    #originalNumbers and convertedNumbers, do the following.
    for original, converted in zip(originalNumbers, convertedNumbers):
        #Display the original next to the converted.
        print(f"{original}\t{converted}")

#Call the main module to run the code properly.
if __name__ == "__main__":
    main()
        
