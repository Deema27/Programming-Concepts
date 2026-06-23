'''Description:
Translates text from an input file into Pig Latin
and writes the translated text to an output file.'''


#Function that converts text into Pig Latin
def pig_latin_translator(text):

    #Split text into individual words
    words = text.split()

    #Create an empty list to store translated words
    pig_latin_version = []

    #Loop through each word in the text
    for word in words:

        #Handle single-letter words
        if len(word) == 1:
            pig_latin_version1 = word + 'ay'

        #Move the first letter to the end and add "ay"
        else:
            pig_latin_version1 = word[1:] + word[0] + 'ay'

        #Add translated word to the list
        pig_latin_version.append(pig_latin_version1)

    #Join translated words back into a single string
    return ' '.join(pig_latin_version)


def main():

    #Ask user for input and output file names
    input_file_name = input("Enter the name of the input text file: ")
    output_file_name = input("Enter the name of the output text file: ")

    #Open and read the input file
    with open(input_file_name, 'r') as input_file:
        text = input_file.read().strip()

    #Translate the text into Pig Latin
    pig_latin_text = pig_latin_translator(text)

    #Open the output file and write translated text
    with open(output_file_name, 'w') as output_file:
        output_file.write(pig_latin_text)


#Call the main function
main()
