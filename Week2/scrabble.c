#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Store the points in an array
int POINTS[]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};

//Declare functions
int calculate_score(string word);

int main(void)
{
    //Prompt user for a word
    string word1 = get_string("Player 1: \n");

    //Prompt user for a second word 
    string word2 = get_string("Player 2: \n");

    //use the function and the first word as input and store the result in variable
    int score1 = calculate_score(word1);

    //use the function and the second word as input and store the result in variable
    int score2 = calculate_score(word2);

    //Check variable condition
    if( score1 > score2)
    {
        //print result if score1 is bigger than score2
        printf("Player 1 wins!\n");

    //Check variable condition
    }else if (score1 < score2)
    {
        //print result if score2 is bigger than score1
         printf("Player 2 wins!\n");

    }else
    {
        //Print Tie is the scores are equal
         printf("Tie!\n");
    }

}

//Function to calculate the score of each word
int calculate_score(string word)
{
    // Variable to keep track of score
    int score = 0;

    // Calulate score for each character
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        //check if the word has uppercase letters
        if (isupper(word[i]))
        {
            //add the points to the score variable
            score += POINTS[word[i] - 'A'];
        }
        //check if the word has lowercase letters
        else if (islower(word[i]))
        {
            //add the points to the score variable
            score += POINTS[word[i] - 'a'];
        }
    }
    //return the score
    return score;
}
