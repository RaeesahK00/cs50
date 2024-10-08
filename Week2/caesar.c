#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

                                                                //declare prototypes
bool only_digits(string s);
char rotate(char s, int n);

                                                                // create a main that takes in a argument
int main(int argc, string argv[])
{

    if (argc != 2)                                              //check that the number of arguments entered is not more than 2
    {
        printf("Usage: ./caesar key\n");                        //prints out error message
        return 1;                                               //returns 1 to end the program as an error occured
    }

    if (only_digits(argv[1]) == false)                          //calls method to check if only digits are being entered in the comand-line argument
    {
        printf("Usage: ./caesar key\n");                        //prints out error message
        return 1;                                               //returns 1 to end the program as an error occured
    }

    int position = atoi(argv[1]);                               //change the comand-line argument from a string to an int

    string plaintext = get_string("plaintext:  ");              //prompt the user for plaintext
    printf("ciphertext:  ");                                    //print out the word ciphertext

    for (int i = 0, l = strlen(plaintext); i < l; i++)          //loop through the plaintext entered by the user
    {

        char ciphertext = rotate(plaintext[i], position);       //use the method rotate to rotate the plaintext entered according to the key and store it in the variable ciphertext
        printf("%c", ciphertext);                               //print the rotated characters
    }
    printf("\n");                                               //print a new line space
    return 0;                                                   // return 0 to end the program sucessfully
}

bool only_digits(string s)                                      //create method to check if the given string only contains digits
{
    for (int i = 0, l = strlen(s); i < l; i++)                  //loop through the string entered, using the length of the string
    {
        if (isdigit(s[i]) == 0)                                 //check if isdigit equals 0 ,meaning the character is not a digit
        {
            return false;                                       //return false
        }
    }
    return true;                                                //return true if it's a digit
}

char rotate(char text, int key)                                 //create method to rotate the plaintext entered by the user
{
    if (isalpha(text))                                          //check if the text entered in alphabetical
    {
        if (isupper(text))                                      //check if the text is uppercase
        {
            text = ((text - 'A' + key) % 26) + 'A';             //subtract the ASCII value of 'A' from any uppercase letters then add it back

        }
        else if (islower(text))                                 //check if the text is lowercase
        {
            text = ((text - 'a' + key) % 26) + 'a';             //subtract the ASCII value of 'a' from any lowercase letters then add it back
        }
    }
    return text;                                                //if the char is not a letter, it should return the same char unchanged
}
