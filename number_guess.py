
# This is a simple number guessing game

Correct_number = 7

# for number in range(100):
while True:
	print('\nThis is a number guessing game.')
	print('I am thinking of a number between 1 and 10.')
	
	chosen_number = int(input('\nPlease guess a number: '))
	
	if chosen_number == Correct_number:
		print('\nGreat job, you guessed my number!')
		break
	else:
		print('\nSorry, that is not my number. Please try again.')