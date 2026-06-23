''' Description:
Executes a two-player trivia game using a list of
trivia questions and keeps track of each player's score.'''

import TriviaQns


#Main function that runs the trivia game
def trivia_game():

    #Create list of trivia questions
    trivia_questions = TriviaQns.create_list()

    #Initialize player scores
    player1_score = 0
    player2_score = 0

    #Get total number of questions
    total_questions = len(trivia_questions)

    #Loop through all questions
    for i in range(total_questions):

        #Get current question object
        question = trivia_questions[i]

        #Alternate between Player 1 and Player 2
        if i % 2 == 0:
            print(f"Question for the first player:")
            player = 1
            player_score = player1_score
        else:
            print(f"Question for the second player:")
            player = 2
            player_score = player2_score

        #Display question and answer choices
        print(question.get_question())
        print(f"1. {question.get_answer1()}")
        print(f"2. {question.get_answer2()}")
        print(f"3. {question.get_answer3()}")
        print(f"4. {question.get_answer4()}")

        #Get player's answer
        player_answer = int(input("Enter your solution (a number between 1 and 4): "))

        #Check if answer is correct
        if player_answer == question.get_correct_answer():
            print("That is the correct answer.\n")

            #Update score for Player 1
            if player == 1:
                player1_score += 1

            #Update score for Player 2
            else:
                player2_score += 1

        #Handle incorrect answer
        else:
            print(f"That is incorrect. The correct answer is {question.get_correct_answer()}\n")

    #Display final scores
    print(f"The first player earned {player1_score} points.")
    print(f"The second player earned {player2_score} points.")

    #Determine winner
    if player1_score > player2_score:
        print("The first player wins the game.")

    elif player2_score > player1_score:
        print("The second player wins the game.")

    else:
        print("The game is a tie.")


#Start the trivia game
trivia_game()
