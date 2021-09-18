
# Andrew Schaefer
# 4/13/21
# Module 6 Assignment, Dictionary

# This is a dictionary of my favorite books
# and the authors who wrote them.

favorite_books = {
	'arguably' : 'christopher hitchens',
	'1984' : 'george orwell',
	'the elegant universe' : 'brian greene',
	'the next 100 years' : 'george friedman',
	'the accidental superpower' : 'peter zeihan',
	'five families' : 'selwyn raab',
	'homo deus' : 'yuval noah harari',
	'the martian' : 'andy weir',
	'farenheit 451' : 'ray bradbury',
	'small is beautiful' : 'e.f. schumacher',
	'brave new world' : 'aldous huxley',	
}
# This displays the titles (keys) of all the books
# within the dictionary.

print(f'\nHere is a list of my favorite books:')
for key in favorite_books:
	print(f'\t{key.title()}')

# This prompts the user for a book of which they
# would like to know the author.

chosen_book = str(input(f'\nPlease enter a book title '
	'to know the author: '))

# If the book entered by the user is in the dictionary,
# this will display the author of the book. If the user
# enters an unrecognized title, an error message will 
# display.

if chosen_book in favorite_books:
	print(f'\nThe author of {chosen_book.title()}' 
		f' is {favorite_books [chosen_book].title()}.')
else:
	print(f"\nI'm sorry, that book is not on my list.")

exit()
