#Victoria Buckner
#CS 120 01
#
#

PACKAGE_PRICE = 99
DISCOUNT_50 = 100
DISCOUNT_40 = 50
DISCOUNT_30 = 20
DISCOUNT_20 = 10

package_number = int(input("Enter the number of packages purchased:"))

if package_number >= DISCOUNT_50:
    price50 = PACKAGE_PRICE*package_number
    discount50 = price50*0.5
    total50 = price50-discount50
    print("The discount is:$", discount50)
    print("The total price after the discount is:$", total50)
elif package_number >= DISCOUNT_40:
    price40 = PACKAGE_PRICE*package_number
    discount40 = price40*0.4
    total40 = price40-discount40
    print("The discount is:$", discount40)
    print("The total price after the discount is:$", total40)
elif package_number >= DISCOUNT_30:
    price30 = PACKAGE_PRICE*package_number
    discount30 = price30*0.3
    total30 = price30-discount30
    print("The discount is:$", discount30)
    print("The total price after the discount is:$", total30)
elif package_number >= DISCOUNT_20:
    price20 = PACKAGE_PRICE*package_number
    discount20 = price20*0.2
    total20 = price20-discount20
    print("The discount is:$", discount20)
    print("The total price after the discount is:$", total20)
else:
    print("There is no discount for this number of packages.")
    
