# Laboratory 2 - Installment 2: Talking to the User
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

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)

print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")

print("-" * 40)

print("Made by: Ivan P. Toledo  |  Installment 2")