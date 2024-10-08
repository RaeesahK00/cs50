from cs50 import get_int                                #import cs50 library to use get_int

def main():                                             #create a main function

    original_number = 0                                 #initialize original_number to 0

    while True:                                         #create a while loop
        card_number = get_int("Number: ")               #prompt the user to enter a card number

        original_number =  card_number                  #store the card number in original_number, to be used for the checksum and length

        while card_number >= 100:                       #Create a loop to get the first 2 digits
            card_number = card_number // 10             #reduces card_number to the first two digits using integer division "//"

        if 10 < card_number < 99:                       #create if statement to check that card_number is between 10 and 99
            break                                       #break when true

    if checksum(original_number):                       #This if statement calls the checksum function to varify if the card is valid

        if(card_number == 34 or card_number == 37) and length(original_number) == 15:                           #check if its a "AMEX" card by checking the first 2 digits and the length
            print("AMEX")                                                                                       #print out the "AMEX" if true

        elif 51 <= card_number <= 55 and length(original_number) == 16:                                         #check if its a "MASTERCARD" card by checking the first 2 digits and the length
            print("MASTERCARD")                                                                                 #print out the "MASTERCARD" if true

        elif card_number // 10 == 4 and (length(original_number) == 13 or length(original_number) == 16):       #check if its a "VISA" card by checking the first 2 digits and the length
            print("VISA")                                                                                       #print out the "VISA" if true

        else:
            print("INVALID")                            #prints "Invalid" if it doesn't match any known card type
    else:
        print("INVALID")                                #prints "Invalid" if checksum validation fails


def length(card_number):                                #function to get the length of the card_number
    return len(str(card_number))                        #get the length by converting the card_number to a string


def checksum(card_number):                              #function to validate the checksum
    total_sum = 0                                       #variable to store the sum of the digits
    is_second_digit = False                             #used to track if the digit must be doubled

    while card_number > 0:                              #while the card_number = 0

        digit = card_number % 10                        #get the last digit in the card number
        card_number = card_number // 10                 #remove the last digit


        if is_second_digit:                             #check if it is every second digit
            digit *= 2                                  #if true times the digit by 2

            if digit > 9:                               #check if the digit is greater than 9
                digit -= 9                              #adjust the digit so that it does not become greater than 9


        total_sum += digit                              #add the digit value to sum
        is_second_digit = not is_second_digit           #switch the boolean, example we started on it being false , next iteration it will be true

    return (total_sum % 10 == 0)                        #return the result and check if sum is divisible by 10


main()                                                  #call the main method
