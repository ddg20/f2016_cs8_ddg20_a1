#name:          Dhruv Gohel
#email:         ddg20@pitt.edu
#date:          09/08/2016
#class:         CS0008-f2016
#instructor:    Max Novelli
#
#description:   Introduction to programming with Python, Chapter 2, Exercise 7
#
#Notes:

milesDriven = int(input("How many miles have you driven?"))
gallonsGas = int(input("How many gallons of gas have you used?"))

kilometers = (milesDriven * 1.60934)
liters = (gallonsGas * 3.78541)
litersPer100Km = (100 * liters / kilometers)

print("")
print("You have driven",kilometers,"km")
print("You have used",liters,"liters")
print("L per 100Km is",litersPer100Km)
