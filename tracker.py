# Laboratory 3 - Installment 3: The Tracker Does Math
# Author: Ivan P. Toledo
# A simple landing page for a personal expense tracker.

print("=" * 40)
print(" " * 12 + "EXPENSE TRACKER")
print(" " * 4 + "Your wallet called. It wants answers.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")

print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

subtotal = 0
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

subtotal += amount2

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * tax_percent / 100

total = subtotal + tax

budget = float(input("Your budget? "))

over_budget = total > budget
left = budget - total

print()
print("-" * 40)

print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")

print("-" * 40)

print("Made by: Ivan P. Toledo  |  Installment 3")