#include <cs50.h>
#include <stdio.h>

// Declared functions
int length(long num);
int checksum(long num);

int main(void)
{
    // Create variable to store the input in
    long num;
    // Create variable to store length of the digit
    long digitLength = 0;

    do
    {
        //Prompt the user for a card number
        num = get_long("Number: ");

        //Add the number entered into digitLength
        digitLength += num;

        // Create a loop to get the first 2 digits
        while (num >= 100)
        {
            //reduces num to the first two digits
            num = num / 10;
        }
    }
    // The while condition ensures that num is between 10 and 99
    while (num < 10 || num > 99);

    // This if statement calls the checksum function to varify if the card is valid
    if (checksum(digitLength))
    {

        //checks if its a AMEX card
        if (num == 34 || num == 37)
        {
            //checks the card type based on the condition
            if (length(digitLength) == 15)
            {
                //prints "AMEX" if length is 15
                printf("AMEX\n");
            }
            else
            {
                //prints "Invalid" if length is not 15
                printf("INVALID\n");
            }
        }
        //checks if its a MASTERCARD card
        else if (num >= 51 && num <= 55)
        {
            //checks the card type based on the condition
            if (length(digitLength) == 16)
            {
                //prints "MASTERCARD" if length is 16
                printf("MASTERCARD\n");
            }
            else
            {
                //prints "Invalid" if length is not 16
                printf("INVALID\n");
            }
        }
        //checks if its a VISA card
        else if (num / 10 == 4)
        {
            //prints "VISA" if length is 13 OR 16
            if (length(digitLength) == 13 || length(digitLength) == 16)
            {
                printf("VISA\n");
            }
            else
            {
                //prints "VISA" if length is not 13 OR 16
                printf("INVALID\n");
            }
        }
        else
        {
            //prints "Invalid" if it doesn't match any known card type
            printf("INVALID\n");
        }
    }
    else
    {
        //prints "Invalid" if checksum validation fails
        printf("INVALID\n");
    }
}

int checksum(long num)
{
    //variable to store the sum of the digits
    int sum = 0;

    //used to track if the digit must be doubled
    int isSecond = 0;

    //variable for storing last digit
    int digit;

    while (num > 0)
    {
        //get the last digit
        digit = num % 10;

        //remove the last digit
        num = num / 10;

        if (isSecond)
        {
            //if it is the second digit4 double the digit
            digit *= 2;
            if (digit > 9)
            {
                //adjust for digits greater than 9
                digit = digit - 9;
            }
        }
        //add the digit to the sum
        sum = sum + digit;
        // switch isSecond
        isSecond = !isSecond;
    }

    //return the result and check if sum is divisible by 10
    return (sum % 10 == 0);
}

int length(long num)
{
     //variable to store the length of the digits
    int length = 0;

    while (num != 0)
    {
        //get last digit
        num = num / 10;
        //increment length
        length++;
    }
    //returns the length of the digit
    return length;
}
