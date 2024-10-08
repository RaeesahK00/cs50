#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string s);

int main(int argc, string argv[])
{

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if(only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int atoi(argv[1]);

        return 0;


}

bool only_digits(string s)
{

    for( int i = 0 , l = strlen(s); i < l; i++)
    {
        if(isdigit(s[i]))
        {
            return true;
        }
    }
     return false;
}

