# Shekinah Tong

# 09/30/2024

# P2HW1

# This program calculates and displays travel expenses, including destination, fuel, accommodation, and food costs, and the remaining budget.



# Start of program

# Get user inputs

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")



# Gather travel expenses

fuel = float(input("How much do you think you will spend on gas? "))

accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))



# Calculate remaining balance

total_expenses = fuel + accommodation + food

remaining_balance = budget - total_expenses



# Display travel expenses

print("\n------------Travel Expenses------------")

print(f"{'Location:':<20} {destination}")

print(f"{'Initial Budget:':<20} ${budget:.2f}")

print(f"{'Fuel:':<20} ${fuel:.2f}")

print(f"{'Accommodation:':<20} ${accommodation:.2f}")

print(f"{'Food:':<20} ${food:.2f}")

print("---------------------------------------")

print(f"{'Remaining Balance:':<20} ${remaining_balance:.2f}")