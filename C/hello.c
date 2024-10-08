//Include library's
#include <stdio.h>
#include <cs50.h>

int main(void){

    // Prompt the user for a name
    string name = get_string("Whats you name? ");
    //Display the name entered
    printf("hello, %s\n", name);

}
