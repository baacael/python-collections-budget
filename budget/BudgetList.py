import Expense

class BudgetList():
    def __init__(self,budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses =[]
        self.sum_overages = 0
        self.overages =[]

def main():
    myBudgetList = BudgetList.budget
    budget = 1200

        
# Define an append method that has two parameters - self and item. Put pass inside the method for now.

def append(self, item):
    if self.sum_expenses + item < self.budget:
       self.expenses.append(item)

    else:
        self.overages.append(item)
        self.sum_overages += item

    
#Replace pass with an if statement that checks if self.sum_expenses 
#plus the passed-in item is less than self.budget. 

#Inside the if block, call append() on self.expenses 
#and pass in item. Also inside the if block, add item to self.sum_expenses.

#After the if block, 
#add an else block that calls append() on self.overages and passes in item. Also, increase self.sum_overages by item.
def __len__(self):
    return self.expenses.len(), self.overages.len()


#After the BudgetList class, define a main() function. Inside of main(), 
#create a myBudgetList variable and assign it a call to the BudgetList constructor with a budget argument of 1200.

#Define a method called __len__ that takes in self as a parameter. 
#Inside the method, return the sum of the length of self.expenses and the length of self.overages.

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#After reading the expenses, create a for loop that has an iterator called expense and loops through expenses.list. 
#Inside the for loop, call append(), with expense.amount as an argument, on myBudgetList.

for expense in expenses.list:
     myBudgetList(append(expense.amount))

#for expense in expenses.list:
 #   spending_categories.append(expense.category)