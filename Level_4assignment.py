expenses = []

while True:
    expense = float(input("Enter an expense or 0 to finish: "))
    #Ensure expense values entered are valid
    if expense == 0:
        break
    elif expense < 0:
        print("Please enter a positive number")
    else:
        expenses.append(expense)

#Make lists you can assign numbers to
small_expense = []
moderate_expense = []
large_expense = []

#Assigning numbers to list so we can count the length later
for amount in expenses:
    if amount < 25:
        small_expense.append(amount)
    elif amount <= 100:
        moderate_expense.append(amount)
    else:
        large_expense.append(amount)

#Make expense summary
print("EXPENSE SUMMARY")

#Make sure the summary only runs if expenses are entered to avoid errors
if len(expenses) > 0:
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total: ${sum(expenses):,.2f}") 
    print(f"Average: ${(sum(expenses))/(len(expenses)):,.2f}")
    print(f"Smallest expense: ${min(expenses):,.2f}")
    print(f"Largest expense: ${max(expenses):,.2f}")

    print(f"Small expenses: {len(small_expense)}")
    print(f"Moderate expenses: {len(moderate_expense)}")
    print(f"Large expenses: {len(large_expense)}")

else:
    print("No expenses were entered.")
