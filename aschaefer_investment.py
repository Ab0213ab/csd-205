
# Andrew Schaefer
# 4/19/21
# Module 7 Assignment, Investment Program

# This program calculates the compound annual interest
# for a given investment & then determines how many
# years it will take to see the principle doubled.
message = 'This is a program that will help you '
message += 'determine how many years it will take '
message += 'to double your investment.'
print(message)

# User inputs both principle & interest rate. 
principle = int(input('\nEnter the principle amount'
' invested: $'))
rate = float(input('\nEnter the annual interest rate: '))
future_amount = principle
years = 0

# Each iteration in while loop calculates the interest
# gained, adds it to principle amount, & continues
# until principle is doubled.
while future_amount < principle * 2:
	future_amount = principle * rate + future_amount
	years += 1

	# Once principle is doubled, loop ends & prints 
	# how many iterations (years) it took to double
	# principle.
	if future_amount >= principle * 2:
		print(f'\nIt will take {years} years to double'
		' your investment.')
		break 