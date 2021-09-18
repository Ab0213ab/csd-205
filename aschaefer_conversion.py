
# Andrew Schaefer
# 4/24/21
# Module 8 Assignment, Conversion Program


print(f'\nThis program will help you convert '
	'miles to kilometers.')

def conversion(miles):
	"""Calculates miles to km conversion & prints the results."""
	kilometers = miles * 1.6
	print(f'\n{miles} miles converts to {kilometers} kilometers.')

# Loop allows user to try again after incorrect entry
while True:
# Try validates user input is an integer & calls function
	try:
		miles = int(input(f'\nPlease enter the number of'
		' miles you wish to convert: '))
		conversion(miles)
		break
# Except gives custom error message if incorrect value is entered.
	except ValueError:
		print(f"\nYour entry was not a valid number, please try again.")
