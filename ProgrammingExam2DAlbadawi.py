''' Description:
Keeps track of the amount of money spent during
a shopping spree and displays spending information,
stores visited, and whether the user stayed within budget.'''

class Spree:

    #Class variable to store the shopping budget
    budget = 0

    #Constructor initializes store name and amount spent
    def __init__(self, store, amount_spent):
        self.__store = store
        self.__amount_spent = amount_spent

    #Returns the amount spent at the store
    def get_amount_spent(self):
        return self.__amount_spent

    #Updates the shopping budget
    def mutate_budget(new_budget):
        budget = new_budget

    #Returns a formatted string representation of the object
    def __str__(self):
        return (f'Store: {self.__store}           Amount Spent: ${self.__amount_spent}')


#Create an empty list to store Spree objects
objects = []

#Function to create and store shopping entries
def create_list(num_stores):

    #Loop through the number of stores visited
    for i in range(1, num_stores + 1):

        #Ask user for store name
        name = input('Name of store: ')

        #Ask user for amount spent
        amt_spent = float(input('Amount spent in store: $'))

        #Create a Spree object
        items = Spree(name, amt_spent)

        #Add object to the list
        objects.append(items)

#Function to calculate total amount spent
def calculate_spent(objects):

    #Initialize total spending
    total = 0

    #Loop through all objects in the list
    for i in objects:

        #Get amount spent from the object
        amount = i.get_amount_spent()

        #Add amount to total
        total += amount

    #Return total amount spent
    return total

#Function to display shopping information
def display(objects):

    #Loop through all objects and print them
    for item in objects:
        print(item)

#Ask user for their budget
budget1 = float(input('What is the maximum amount you want to spend? $'))

#Ask user for number of stores visited
stores_visited = int(input('Enter number of stores visited (where a purchase was made): '))

#Update the class budget
Spree.mutate_budget(budget1)

#Create shopping entries
create_list(stores_visited)

#Display budget information
print(f'Your budget was ${budget1}')

#Display stores and spending information
display(objects)

#Display total amount spent
print(f'You spent ${calculate_spent(objects):,.2f}')

#Check if the user stayed within budget
if calculate_spent(objects) <= budget1:
    print(f'Yay! You stayed within the budget!')

#Display how much the user went over budget
else:
    difference = calculate_spent(objects) - budget1
    print(f'Yikes, you spent ${difference:,.2f} over your budget.')
                           
