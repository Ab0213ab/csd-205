
#Andrew Schaefer
#3/31/21
#Module 4 Assignment, Tuple

airport_codes = ('MCO','LGA','MIA','CDG',
	'LAX','HNL','LAS','BCN','LHR','PHL',
	'GRU','FNJ','MBJ','BKK','NRT')

# Displays the airport codes in the tuple.
print(f'\n{airport_codes}')

# For loop displays a string for every
# airport code in the tuple.
for airport_code in airport_codes:
	print(f"\nWhen the pandemic is over I'm "
		f"flying to {airport_code.upper()}!")

# For loop displays a string for every
# airport code in the tuple in reverse order.
reversed_tuple = tuple(reversed(airport_codes))
for airport_code in reversed_tuple:
	print(f"\nWhen the pandemic is over I'm "
		f"flying to {airport_code.upper()}!")

