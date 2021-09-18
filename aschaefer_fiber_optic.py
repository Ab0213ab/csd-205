
#Andrew Schaefer
#3/27/21
#Module 3, Fiber Optic Program

#This program helps the user calculate
#the cost of their fiber optic cable.

message = "Hello, please enter your company name."
print(message)

company_name = input()
feet = int(input("\nPlease enter how many feet of fiber optic cable you would like: "))

cost_per_foot = .87
total = (cost_per_foot * feet)

message = f"\nThank you, {company_name.title()}, your cost is ${total}. Have a great day."
print(message)
exit()