
# Andrew Schaefer
# 4/28/21
# Module 9 Assignment, Classes


class BankAccount:
	"""A simple representation of a bank account"""

	def __init__(self, account_number, balance):
		"""Initialize account number and balance attributes"""
		self.account_number = account_number
		self.balance = balance

	def make_withdrawl(self):
		"""Subtracts user input from current balance and displays 
		the remaining balance."""
		withdrawl = int(input(f'How much do you want to withdrawl? $'))
		post_withdrawl_amount = self.balance - withdrawl 
		print(f'Your new balance after your withdrawl is ${post_withdrawl_amount}.')

	def make_deposit(self):
		"""Adds user input to the current balance and displays the new balance."""
		deposit = int(input(f'How much do you want to deposit? $'))
		post_deposit_amount = self.balance + deposit
		print(f'Your new balance after your deposit is ${post_deposit_amount}.')

	def get_balance(self):
		"""Displays the user's current balance."""
		print(f'Your balance is ${self.balance}.')



class CheckingAccount(BankAccount):
	"""A simple representation of a checking account"""

	def __init__(self, account_number, balance):
		"""Initialize attributes of the parent class."""
		super().__init__(account_number, balance)
		self.fees = 5
		self.minimum_balance = 50

	def deduct_fees(self):
		"""Subtracts the fees from the user's current balance and displays
		the new balance."""
		post_deduction_amount = self.balance - self.fees
		print(f'Your balance after the fees is ${post_deduction_amount}.') 

	def check_minimum_balance(self):
		"""Runs a conditional test on the user's current balance
		and displays a message depending on the results."""
		if self.balance < self.minimum_balance:
			print(f'Your account balance is below the minimum.')
		else:
			print(f'Your account balance is above the minimum.')

class SavingsAccount(BankAccount):
	"""A simple representation of a savings account"""

	def __init__(self, account_number, balance):
		"""Initialize attributes of the parent class."""
		super().__init__(account_number, balance)
		self.interest_rate = .02

	def add_interest(self):
		"""Adds interest based on a default rate to the user's
		current balance and displays the new amount."""
		post_interest_amount = self.balance * self.interest_rate + self.balance
		print(f'Your balance after adding interest is ${post_interest_amount}.')


print(f'\nWelcome to your personal online banking application.')

while True: 
#Loop allows user to continue input until valid account number is entered,
#and exits the loop once this has occured.

	try:
		#Try/except blocks validate user account number
		account_number = int(input('Enter your account number (for the sake of brevity,'
			' the only valid account numbers are 1 or 2: '))
		
		#IF chain sets account balance based on the account number
		if account_number == 1:
			balance = 200
			break
		if account_number == 2:
			balance = 25
			break

	except ValueError:
		print(f'\nSorry, your account number is invalid.')

while True:
#Loop allows user to continue input until valid account choice is entered,
#and exits the loop once this has occured.

	try:
		#Try/except blocks validate user account choice
		chosen_account = int(input(f'Which account would you like to access?'
		'\nEnter "1" for checking, "2" for savings, or "3" to exit. '))
		
		#If/else chain allows loop to be exited once a valid account choice has been 
		#entered or if the user chooses to exit via #3
		if chosen_account == 1 or 2:
			break
		if chosen_account == 3:
			exit()
		else:
			print('Please enter a "1" or "2".' )

	except ValueError:
		print(f'\nSorry, your choice was invalid. Please enter "1" or "2".')

while chosen_account == 1:
	#Loop allows user to continue using the program until ready to exit

	try:
		#Try/except blocks validate user menu choices

		print(f'\nChecking Function Menu:')
		print(f'\n\t1. Make a Withdrawl'
		'\n\t2. Make a Deposit'
		'\n\t3. Display My Balance'
		'\n\t4. Deduct Fees'
		'\n\t5. Check Minimum Balance'
		'\n\t6. Exit Program')
		choice = int(input(f'\nPlease enter the number of your choice: '))
		
		#If/elif/else chain allows user to make a choice of which account function to run,
		#including exiting the loop.
		if choice == 1:
			inst_1 = BankAccount(account_number, balance)
			inst_1.make_withdrawl()
		elif choice == 2:
			inst_2 = BankAccount(account_number, balance)
			inst_2.make_deposit()
		elif choice == 3:
			inst_3 = BankAccount(account_number, balance)
			inst_3.get_balance()
		elif choice == 4:
			inst_4 = CheckingAccount(account_number, balance)
			inst_4.deduct_fees()
		elif choice == 5:
			inst_5 = CheckingAccount(account_number, balance)
			inst_5.check_minimum_balance()
		elif choice == 6:
			break
		else:
			print(f'\nPlease enter a valid number choice.')

	# Displays a custom error message.	
	except ValueError:
		print(f'\nSorry, your choice was invalid. Please enter a number.')

while chosen_account == 2:
#Loop allows user to continue using the program until ready to exit.

	try:
	#Try/except blocks validate user menu choices

		print(f'\nSavings Function Menu:')
		print(f'\n\t1. Make a Withdrawl'
		'\n\t2. Make a Deposit'
		'\n\t3. Display my Balance'
		'\n\t4. Add Interest'
		'\n\t5. Exit Program')
		choice = int(input(f'\nEnter the number of your choice: '))

		#If/elif/else chain allows user to make a choice of which account function to run,
		#including exiting the loop.
		if choice == 1:
			inst_1 = BankAccount(account_number, balance)
			inst_1.make_withdrawl()
		elif choice == 2:
			inst_2 = BankAccount(account_number, balance)
			inst_2.make_deposit()
		elif choice == 3:
			inst_3 = BankAccount(account_number, balance)
			inst_3.get_balance()
		elif choice == 4:
			inst_4 = SavingsAccount(account_number, balance)
			inst_4.add_interest()
		elif choice == 5:
			break
		else:
			print(f'\nPlease enter a valid number choice.')

	# Displays a custom error message.	
	except ValueError:
		print(f'\nSorry, your choice was invalid. Please enter a number.')

