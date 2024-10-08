#include <cs50.h>
#include <stdio.h>

int main(void)
{

int height ;

do
{
    //prompt user for height

    height = get_int("Height: ");
}
    //make sure the user can only enter a number from 1-8
while(height < 1 || height > 8 );

    //print height of pramid

    for(int i = 1; i <= height;i++)
    {
        //print left spaces of pramid
        for(int a = height - i ; a > 0 ; a--)
        {
            printf(" ");
        }

        //print right side of bricks
        for(int b = 1; b <= i ; b++)
        {
            printf("#");
        }

        //print middle 2 spaces
         for(int a = 2 ; a > 0 ; a--)
        {
            printf(" ");
        }

        //print left side of bricks
         for(int b = 1; b <= i ; b++)
        {
            printf("#");
        }

        //create a new line
        printf("\n");

    }



}

