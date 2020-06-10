# importing the sys doc
import sys

# variable block
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00
amtDue = baseCharge + mileCharge

rentalCode = input ('(B)udget, (D)aily, or (W)eekly rental? \n')

# prompt selection based off of day budget or week rental
if rentalCode == "B" or rentalCode == "D":
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))

# base charge calculation
if rentalCode == "B":
  baseCharge = float(rentalPeriod * budgetCharge)
elif rentalCode == "D":
  baseCharge = float(rentalPeriod * dailyCharge)
elif rentalCode == "W":
  baseCharge = float(rentalPeriod * weeklyCharge)

#Odometer calculation
odoStart = input( "Starting Odometer Reading:\n")

odoEnd = input("Ending Odometer Reading:\n")

totalMiles = int(odoEnd) - int(odoStart)






#milecharge based off of type of rental and mileage

if rentalCode == "B":
  mileCharge = int(totalMiles) * 0.25

  if rentalCode == "D":
    averageDayMiles = int(totalMiles)/int(rentalPeriod)
  if averageDayMiles <= 100:
    totalMilesMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
  mileCharge = 0.25 * extraMiles

elif rentalCode == "W":
  averageWeekMiles = int(totalMiles)/int(rentalPeriod)
  mileCharge = 0
  if averageWeekMiles > 900:
    mileCharge = 100.00 * int(rentalPeriod)
  else:
    mileCharge = 0.00

# Statment printout

print('Rental Summary')
print('Rental Code:        '+ str(rentalCode))
print('Rental Period:        '+ str(rentalPeriod))
print('Starting Odometer:  '+ str(odoStart))
print('Ending Odometer:    '+ str(odoEnd))
print('Miles Driven:       '+ str(totalMiles))
print('Amount Due:    '+'     ${:,.2f}'.format(amtDue))
