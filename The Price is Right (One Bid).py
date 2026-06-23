''' Description:
Determines which player's bid is closest to the
actual price in a game inspired by "The Price is Right!".'''

import random

#Generate a random actual price between 1000 and 5000
actual_price = random.randint(1000, 5000)

#Create an empty list to store player bids
bids = []

#Loop to get bids from 4 players
for i in range(1, 5):

    #Ask the current player for their bid
    bid = int(input(f"Player {i}, what is your bid? "))

    #Add the bid to the list
    bids.append(bid)

#Check if all players overbid
if all(bid > actual_price for bid in bids):
    print("Buzz! Aww... everyone has overbid!")

#Check if any player guessed the exact price
elif actual_price in bids:

    #Find the winning player's number
    winner = bids.index(actual_price) + 1

    #Display winning message
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f"Actual price is ${actual_price}! Player {winner}, come on up!")

else:

    #Create a list to store valid bids
    valid_bids = []

    #Loop through all bids
    for bid in bids:

        #Only keep bids that do not exceed the actual price
        if bid <= actual_price:
            valid_bids.append(bid)

    #Find the highest valid bid
    winning_bid = max(valid_bids)

    #Find the winning player's number
    winner = bids.index(winning_bid) + 1

    #Display the winner
    print(f"Actual price is ${actual_price}! Player {winner}, come on up!")  print(f'Actual price is ${actual_price}! Player 4, come on up!')
