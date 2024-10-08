#include <cs50.h>
#include <stdio.h>

// create an array to store all the coins
int coins[] = {25, 10, 5, 1};

// Define the length of the array knowing that it won't change
#define SIZE 4

int main(void)
{
    //create a counter variable which will be the amount of coins
    int counter = 0;
    //create change variable
    int change;

    do
    {
        //prompt the user to enter change owed
        change = get_int("Change owed: ");
    }
    while (change < 0);

    //loop through the array checking each coin
    for (int i = 0; i < SIZE; i++)
    {
        // get the amount of coins from the change then add it to the counter
        counter = counter + change / coins[i];

        //calculate what is left of the change and update the change variable
        change = change % coins[i];
    }
    //print out the amount of coins
    printf("%i\n", counter);
    return 0;

}
