#Victoria Buckner
#CS 120 01
#Chapter 5 Assignment 1
#This program will ask the user for the value
#of a property then calculate the assessed
#value and property tax. Then display the values.

#This function calls for the other functions and
#asks the user to input the actual value of the
#property.
def main():
    actual_value = float(input("Enter the actual value of the property: $"))
    
    assessed_value = calculate_assessed_value(actual_value)
    property_tax = calculate_property_tax(assessed_value)

    display_results(assessed_value, property_tax)

#This function sets the assessment rate and returns
#the sum of the actual value multiplied by the
#assessment rate.
def calculate_assessed_value(actual_value):
    assessment_rate = 0.60
    return actual_value * assessment_rate

#This function sets the tax rate and returns
#the sum of the assessed value divided by 100
#and the tax rate.
def calculate_property_tax(assessed_value):
    tax_rate_per_100 = 0.72
    return (assessed_value / 100) * tax_rate_per_100

#This functions displays the values calculated in
#the previous functions.
def display_results(assessed_value, property_tax):
    print(f"Assessment Value: ${assessed_value:.2f}")
    print(f"Property Tax: ${property_tax:.2f}")
    
if __name__ == "__main__":
    main()
