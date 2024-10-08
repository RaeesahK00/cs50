#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool validate_key(string key);                                                   //declare prototypes
string substitution(string text, string key);

int main(int argc, string argv[])                                                // create a main that takes in a argument
{
    if (argc != 2)                                                               //check that the number of arguments entered is not more than 2
    {
        printf("Usage: ./substitution key\n");                                   //prints out error message
        return 1;                                                                //returns 1 to end the program as an error occured

    }

    if (validate_key(argv[1]) == false)                                         //calls method to validate the key
    {
        return 1;                                                               //returns 1 to end the program as an error occured
    }

    string plaintext = get_string("plaintext:  ");                              //prompts the user to enter plaintext

    string ciphertext = substitution(plaintext,argv[1]);                        //use the method to substitute the plaintext according to the key entered and store it in the variable
    printf("ciphertext:  %s\n", ciphertext);                                    //display the ciphered text

    return 0;                                                                   //return 0 to end the program sucessfully
}



bool validate_key(string key)                                                   //boolean method to validate the key
{
    if (strlen(key) != 26)                                                       //check if the length of the key is not longer than 26 characters
    {
        printf("Key must contain 26 characters.\n");                            //print error message
        return false;                                                           //return false
    }
    else
    {
        for (int i = 0, size = strlen(key); i < size ; i++)                     //create a for loop to loop through the string
        {
            if (!isalpha(key[i]))                                                //check if the key is not alphabetic
            {
                printf("Key must only contain alphabetic characters.\n");       //print error message
                return false;                                                   //return false
            }


            for (int j = i + 1, length = strlen(key); j < length ; j++)          //inner for loop starting at the second index and looping through the string
            {

                if (toupper(key[i]) == toupper(key[j]))                         //convert the key to uppercase and check if the key at index of the first loop is equal to the index of the inner loop
                {
                    printf("Key must not contain repeated characters.\n");      //if they are equal print error message
                    return false;                                               //return false
                }
            }
        }
    }

    return true;                                                                //return true if everything is correct
}



string substitution(string text, string key)                                    //method to substitute the given plaintext according to the key
{
    for (int i = 0, s = strlen(text); i < s; i++)                               // create a for loop to loop through the string
    {
        if (isalpha(text[i]))                                                    //check if the text entered is alphabetic
        {
            if (isupper(text[i]))                                                //check if the text character is uppercase
            {
                int index = toupper(text[i]) - 'A';                             //if the character is uppercase it calculates the position in the alphabet
                text[i] = toupper(key[index]);                                  //this line replaces the original character with the corresponding character from key, ensuring it's also uppercase

            }
            else if (islower(text[i]))                                          //check if the text character is lowercase
            {
                int index = tolower(text[i]) - 'a';                             //if the character is lowercase it calculate the position of the alphabet
                text[i] = tolower(key[index]);                                  //this line replaces the original character with the corresponding character from key, ensuring it's also lowercase
            }
        }
    }
    return text;                                                                // return text after the for loop is completed and the text has been modified
}
