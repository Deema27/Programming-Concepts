''' Description:
Creates a list of trivia questions using a function'''

import Question

#Function to create and return a list of trivia questions
def create_list():

    #Initialize empty list
    question_list = []

    #Add trivia questions to the list
    question_list.append(Question.TQuestion('How many days are in a lunar year?', 354, 365, 243, 379, 1))
    question_list.append(Question.TQuestion('What is the largest planet?', 'Mars', 'Jupiter', 'Earth', 'Pluto', 2))
    question_list.append(Question.TQuestion('What is the largest kind of whale?', 'Orca Whale', 'Humpback Whale', 'Beluga Whale', 'Blue Whale', 4))
    question_list.append(Question.TQuestion('Which dinosaur could fly?', 'Triceratops', 'Tyrannosaurus Rex', 'Pteranodon', ' Diplodocus', 3))
    question_list.append(Question.TQuestion("Which children's story character is a donkey?", 'Pooh', 'Eeyore', 'Piglet', 'Kanga', 2))
    question_list.append(Question.TQuestion('What is the hottest planet?', 'Mars', 'Pluto', 'Earth', 'Venus', 4))
    question_list.append(Question.TQuestion('Which dinosaur had the largest brain compared to body size?', ' Troodon', ' Stegosaurus', 'Ichthyosaurus', ' Gigantoraptor', 1))
    question_list.append(Question.TQuestion('What is the largest type of penguins?', 'Chinstrap penguins', 'Macaroni penguins', 'Emperor penguins', 'White-flippered penguins', 3))
    question_list.append(Question.TQuestion("Which children's story character is a monkey?", "Winnie the Pooh", 'Curious George', ' Horton', 'Goofy', 2))
    question_list.append(Question.TQuestion('How long is a year on Mars?', '550 Earth days', '498 Earth days', '126 Earth days', '687 Earth days', 1))

    #Return the completed list
    return question_list
