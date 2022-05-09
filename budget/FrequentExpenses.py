import Expense

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

#Create an empty list called spending_categories. 
spending_categories = []
#Then, create a for loop with an iterator called expense that loops through expenses.list. 

for expense in expenses.list:
    spending_categories.append(expense.category)

#Inside the loop, we want to append() expense.category to spending_categories.

print(spending_categories)