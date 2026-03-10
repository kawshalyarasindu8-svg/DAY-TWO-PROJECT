# Simple Budget Tracker with Warning

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget (LKR): "))

# Ask for 3 expenses
expense1 = float(input("Enter expense 1 (LKR): "))
expense2 = float(input("Enter expense 2 (LKR): "))
expense3 = float(input("Enter expense 3 (LKR): "))

# Calculate total expenses
total_expenses = expense1 + expense2 + expense3

# Calculate remaining balance
balance = budget - total_expenses

# Display results
print("\nTotal Budget:", budget, "LKR")
print("Total Expenses:", total_expenses, "LKR")
print("Remaining Balance:", balance, "LKR")

# Warning message
if balance < 500:
    print("Warning: Low Funds")