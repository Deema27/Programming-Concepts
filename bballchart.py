'''Description: 
Creates a bar chart showing the points scored
by basketball players during a game.'''

import matplotlib.pyplot as plt

#Create an empty list to store player names
players_names = []

#Loop to get the names of 5 players
for i in range(1, 6):
    player = input(f'Enter the name of player{i}:')
    players_names.append(player)

#Create an empty list to store player points
players_points_list = []

#Loop to get points scored by each player
for i in range(5):

    #Get the current player's name
    current_player = players_names[i]

    #Ask user for the player's points
    player_point = int(input(f'Enter the points earned by {current_player}:'))

    #Validate that points are non-negative
    while player_point < 0:
        player_point = int(input(f'Invalid points entered. Re-enter the points earned by {current_player}:'))

    #Add points to the list
    players_points_list.append(player_point)

#Label the y-axis
plt.ylabel('Points')

#Add a title to the chart
plt.title('Chart showing points scored by each basketball player')

#Create the bar chart
plt.bar(players_names, players_points_list)

#Display the chart
plt.show()
