''' Description:
Creates a class containing a trivia question,
four answer options, and the number of the correct answer.'''

class TQuestion:

    #Constructor initializes question, answers, and correct answer
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct_answer = correct_answer

    #Getter for question
    def get_question(self):
        return self.__question

    #Getter for answer 1
    def get_answer1(self):
        return self.__answer1

    #Getter for answer 2
    def get_answer2(self):
        return self.__answer2

    #Getter for answer 3
    def get_answer3(self):
        return self.__answer3

    #Getter for answer 4
    def get_answer4(self):
        return self.__answer4

    #Getter for correct answer
    def get_correct_answer(self):
        return self.__correct_answer

    #Setter for question
    def set_question(self, question):
        self.__question = question

    #Setter for answer 1
    def set_answer1(self, answer1):
        self.__answer1 = answer1

    #Setter for answer 2
    def set_answer2(self, answer2):
        self.__answer2 = answer2

    #Setter for answer 3
    def set_answer3(self, answer3):
        self.__answer3 = answer3

    #Setter for answer 4
    def set_answer4(self, answer4):
        self.__answer4 = answer4

    #Setter for correct answer
    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer
