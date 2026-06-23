''' Description:
Asks the user to choose between pentagonal,
heptagonal, and hendecagonal sequences, then
displays the sequence values based on the user's choice.'''

def main():

    #Function to display the menu
    def menu():
        print('Welcome to the number sequence generator program!')
        print('Here are your choices:')
        print('1. Pentagonal Sequence')
        print('2. Heptagonal Sequence')
        print('3. Hendecagonal Sequence')
        print()

    #Display menu
    menu()

    #Ask user to choose a sequence type
    choices = int(input('Enter your choice (1-3):'))

    #Validate menu choice
    while choices > 3 or choices < 1:
        choices = int(input('Invalid entry. Re-enter your choice (1-3):'))

    #Ask user for the number of sequence values
    value = int(input('Enter the number of values for the list (>= 3):'))

    #Validate that the value is at least 3
    while value < 3:
        value = int(input('Invalid entry. Re-enter the number of values for the list:'))

    #Function to generate pentagonal sequence
    def pentagonal_sequence(values):

        #Create empty list to store values
        list1 = []

        #Initialize counter
        number = 1

        #Generate sequence values
        while number <= values:

            #Calculate pentagonal number
            answer = ((3 * number ** 2) - number) / 2

            #Convert answer to integer
            answer = int(answer)

            #Add value to list
            list1.append(answer)

            #Increase counter
            number += 1

        #Return completed list
        return list1

    #Function to generate heptagonal sequence
    def heptagonal_sequence(values):

        #Create empty list to store values
        list2 = []

        #Initialize counter
        number = 1

        #Generate sequence values
        while number <= values:

            #Calculate heptagonal number
            answer = ((5 * (number ** 2)) - (3 * number)) / 2

            #Convert answer to integer
            answer = int(answer)

            #Add value to list
            list2.append(answer)

            #Increase counter
            number += 1

        #Return completed list
        return list2

    #Function to generate hendecagonal sequence
    def hendecagonal_sequence(values):

        #Create empty list to store values
        list3 = []

        #Initialize counter
        number = 1

        #Generate sequence values
        while number <= values:

            #Calculate hendecagonal number
            answer = ((9 * (number ** 2)) - (7 * number)) / 2

            #Convert answer to integer
            answer = int(answer)

            #Add value to list
            list3.append(answer)

            #Increase counter
            number += 1

        #Return completed list
        return list3

    #Display pentagonal sequence
    if choices == 1:
        print('Here is a list containing the first', value,
              'numbers of the pentagonal sequence:',
              pentagonal_sequence(value))

    #Display heptagonal sequence
    elif choices == 2:
        print('Here is a list containing the first', value,
              'numbers of the heptagonal sequence:',
              heptagonal_sequence(value))

    #Display hendecagonal sequence
    elif choices == 3:
        print('Here is a list containing the first', value,
              'numbers of the hendecagonal sequence:',
              hendecagonal_sequence(value))


#Call the main function
main()

#Ask user if they want to run the program again
re_run = input('Would you like to run the program again? Enter yes or no:')

#Convert response to lowercase
re_run = re_run.lower()

print()
print()

#Repeat program while user enters yes
while re_run == 'yes':

    #Run the program again
    main()

    #Ask user again if they want to continue
    re_run = input('Would you like to run the program again> Enter yes or no:')

    print()
    print()

#Display goodbye message when user exits
else:
    print('Thanks for using the program! Goodbye!')
