from cs50 import get_string                          #import cs50 library to use get_string


def main():                                         #create a main mthod

    get_text = get_string("Text: ")                 #prompt the user to enter some text

    letters = count_letters(get_text)               #use count_letters function to count the number of letters

    words = count_words(get_text)                   #use count_words function to count the number of words

    sentences = count_sentences(get_text)           #use count_sentences function to count the number of sentences

    L = letters / words * 100                       #find the average number of letters per 100 words in the text

    S = sentences / words * 100                     #find the average number of sentencse per 100 words in the text

    coleman_index = 0.0588 * L - 0.296 * S - 15.8   #calulate Coleman-Liau index

    grade = int(round(coleman_index))               #round off the result of index variable


    if grade < 1:                                   #Check the condition of grade variable to determine the grade
        print("Before Grade 1")                     #if grade value is smaller than 1 print "Before grade 1"
    elif grade >= 16:                               #else if grade bigger than or equal to 16 print "Grade 16+"
        print("Grade 16+")
    else:
        print(f"Grade {grade}")                     #else just print the grade



def count_letters(text):                            #count the amout of letters function
    letter_counter = 0                              #create a counter variable

    for letters in text:                            #loop through the text
        if letters.isalpha():                       #check if it is alphabetic
            letter_counter += 1                     #if true increment letter_counter
    return letter_counter                           #return the letter_counter value


def count_words(text):                             #count the amout of words function
    words_counter = 1                              #create a counter variable initialize to 1 assuming there is already a word present

    for words in text:                             #loop through the text
        if words.isspace():                        #check if there is a space in the string
            words_counter += 1                     #if true increment by 1
    return words_counter                           #return the word_counter value


def count_sentences(text):                                              #count the amout of sentences function
    sentence_counter = 0                                                #create a counter variable

    for sentences in text:                                              #loop through the text
        if sentences == '.' or sentences == '!' or sentences == '?':    #check if the position in the text contains '!' , '.' ,'?'
            sentence_counter += 1                                       #if true increment sentence_counter
    return sentence_counter                                             #return the sentence_counter value


main()                                              #call the main method
