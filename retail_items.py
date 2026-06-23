''' Description:
Prompts the user for the number of items as well as their
names, amounts, and prices, then displays the information
in a formatted table. '''


class RetailItem:

    #Constructor initializes the item's type, price, and amount
    def __init__(self, item_type, item_price, item_amount):
        self.__item_type = item_type
        self.__item_price = item_price
        self.__item_amount = item_amount

    #Returns a formatted string representation of the object
    def __str__(self):
        return f'{self.__item_type:<15} {self.__item_amount:<10} {self.__item_price:>8.2f}'


def main():

    #Ask user how many items they want to add
    num_of_items = int(input("How many items will you add today? "))

    #Validate that the number of items is at least 1
    while num_of_items < 1:
        print("Invalid. Number of items must be at least 1.")
        num_of_items = int(input("How many items will you add today? "))

    #Create an empty list to store RetailItem objects
    items_list = []

    #Loop through each item the user wants to add
    for i in range(1, num_of_items + 1):

        #Get the item name from the user
        type_item = input(f"Name of item {i}: ")

        #Get the item amount
        amount_item = int(input(f"Amount of item {i}: "))

        #Validate that the amount is non-negative
        while amount_item < 0:
            print("Invalid. Amount of numbers must be non-negative.")
            amount_item = int(input(f"Amount of item {i}: "))

        #Get the item price
        price_item = float(input(f"Price of item {i}: "))

        #Validate that the price is non-negative
        while price_item < 0.00:
            print("Invalid. Price must be non-negative.")
            price_item = float(input(f"Price of item {i}: "))

        #Create a RetailItem object using user input
        items = RetailItem(type_item, price_item, amount_item)

        #Add the object to the list
        items_list.append(items)

        print()

    #Display table heading
    print(f"\nHere is a summary of the {num_of_items} items you added:")
    print(f"{'Item':<15} {'Amount':<10} {'Price':>8}")
    print("-" * 45)

    #Print each item in the list
    for item in items_list:
        print(item)


#Call the main function to start the program
main()
