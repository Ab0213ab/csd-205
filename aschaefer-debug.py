# Andrew Schaefer
# 5/9/21
# Module 11, Debug

# This is a simple number guessing game

print(f'\nThis is a simple two player number guessing game.'
	' Player 1 will provide a number and player 2 will'
	' try to guess it.')

# Number to guess is created with user input.
Correct_number = int(input(f'\nPlayer 1 enter your secret number'
	' and then pass the computer to player 2 to guess. '))

# While loop allows multiple attempts.
while True:

	chosen_number = int(input("\nPlayer 2, it's your turn to guess"
	" player 1's secret number: "))

	# If/else chain validates player 2's choice as correct or incorrect.
	if chosen_number == Correct_number:
		print("\nGreat job, you guessed player 1's secret number!")
		break
	else:
		print("\nSorry, that is not player 1's secret number."
			" Please try again.")