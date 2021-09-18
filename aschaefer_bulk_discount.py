# Andrew Schaefer
# 4/2/21
# Module 5, Fiber Optic Program with Bulk Discount Added

# This program helps the user calculate the cost of their
# fiber optic cable purchase, and provides a discount for
# buying in bulk.

company_name = input("Hello, please enter your company name: ")
feet = int(input("\nPlease enter how many feet of fiber optic cable you would like: "))

if feet <= 100:
	cost_per_foot = .87
if feet > 100:
	cost_per_foot = .80
if feet > 250:
	cost_per_foot = .70
if feet > 500:
	cost_per_foot = .50

total = (cost_per_foot * feet)

print(f"\nThank you, {company_name.title()}, your cost is ${total}. Have a great day.")
exit()