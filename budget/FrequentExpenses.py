import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

#Create an empty list called spending_categories. 
spending_categories = []
#Then, create a for loop with an iterator called expense that loops through expenses.list. 
#Inside the loop, we want to append() expense.category to spending_categories.
#print(spending_categories)

for expense in expenses.list:
    spending_categories.append(expense.category)



#We want to use the Counter Collection in order to count which categories had the most purchases.
#To start, import collections at the top of the file. 
#Then after the for loop, create a new variable called spending_counter, 
# set it to an instance of collections.Counter(), and pass spending_categories into the constructor.
spending_counter = collections.Counter(spending_categories)
#print(spending_counter)


#We can get the top 5 most common categories by calling the most_common() method on spending_counter 
#and passing in the value 5. Set the result equal to a variable called top5.

top5 = spending_counter.most_common(5)
#print(spending_counter.most_common(5))

""" If you’ve used the zip() function before it combines 2 iterables. 
(For example, zip(list1, list2) would combine two lists into a list of tuples).
We can also use zip(*dictionary_variable) to separate the keys and values of a dictionary into separate lists. 
Since we want to have 2 separate lists for the categories and their counts for the bar graph, 
let’s call zip(*top5) and set the result equal to two variables - categories, count. """

categories, count = zip(*top5)

fig, ax = plt.subplots()
#Next, call ax.bar() with the categories and count lists as the arguments. On the next line,
# add a title by calling ax.set_title() and pass in the string '# of Purchases by Category'.
ax.bar(categories,count)
ax.set_title('# of Purchases by Category') 

plt.show()