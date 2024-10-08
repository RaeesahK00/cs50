#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Declare functions
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // prompt the user to enter some text
    string text = get_string("Text: ");

    // Use function to count the number of letters
    int letters = count_letters(text);

    // Use function to count the number of words
    int words = count_words(text);

    // Use function to count the number of sentences
    int sentences = count_sentences(text);

    //Find the average number of letters per 100 words in the text
    float L = ((float) letters / words) * 100;

    //Find the average number of sentences per 100 words in the text
    float S = ((float) sentences / words) * 100;

    //compute the Coleman-Liau index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    //Round off the result of index variable
    int grade = (int) round(index);

    // Check the condition of grade variable to determine the grade
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
          printf("Grade %i\n", grade);

        // //check the condition and print the the specific grade
        // switch (grade)
        // {
        //     case 2:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 3:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 5:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 7:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 8:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 9:
        //         printf("Grade %i\n", grade);
        //         break;
        //     case 10:
        //         printf("Grade %i\n", grade);
        //         break;
        //     default:
        //         break;
       // }
    }
}

//Count the amout of letters function
int count_letters(string text)
{
    //create a counter variable
    int count = 0;

    //loop through the length of the text
    for (int i = 0, s = strlen(text); i < s; i++)
    {
        //check if the the text is alphabetic
        if (isalpha(text[i]))
        {
            //increase the counter
            count++;
        }
    }
    //return the amount of letters
    return count;
}

//Count the amout of words function
int count_words(string text)
{
    //create a counter variable
    int count = 1;

    //loop through the length of the text
    for (int i = 0, s = strlen(text); i < s; i++)
    {
        //check for all the spaces
        if (isblank(text[i]))
        {
            //increase the counter
            count++;
        }
    }
    //return the amount of words
    return count;
}

//Count the amount of sentences function
int count_sentences(string text)
{
    //create a counter variable
    int count = 0;

    //loop through the length of the text
    for (int i = 0, s = strlen(text); i < s; i++)
    {
        //check for the punctuation and add to the counter
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            // increase the counter
            count++;
        }
    }
    //return the amount of sentences
    return count;
}
