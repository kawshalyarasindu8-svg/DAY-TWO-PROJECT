# Budget Tracker with Multiple Expenses

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget (LKR): "))

total_expenses = 0

# Loop for entering expenses
while True:
    expense = input("Enter an expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total_expenses += float(expense)

# Calculate remaining balance
balance = budget - total_expenses

# Display results
print("\nTotal Budget:", budget, "LKR")
print("Total Expenses:", total_expenses, "LKR")
print("Remaining Balance:", balance, "LKR")

# Warning if balance is low
if balance < 500:
    print("Warning: Low Funds")