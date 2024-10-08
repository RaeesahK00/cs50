#include <stdio.h>
#include <cs50.h>

int main(void){

    int height;
    do
    {
          //prompt the user for a height
         height = get_int("Height: ");
    }

    while(height < 1);
        //print the height for the pyramid
        for(int i = 1 ; i <= height; i++)
        {
            //print the spaces so that the pyramid leans to the right
            for(int spaces = height - i ; spaces > 0 ; spaces--)
            {
                printf(" ");
            }
            // print the bricks
            for(int bricks = 1 ; bricks <= i ; bricks++)
            {
                    printf("#");
            }

            //create new line
            printf("\n");
        }





}
