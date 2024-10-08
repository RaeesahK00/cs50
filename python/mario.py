from cs50 import get_int  #import cs50 library to use the get_int function

while True:                         #create a while loop , to loop prompting the height until if statement is true
    height = get_int("Height: ")    #prompt the user to enter a height
    if 1 <= height <= 8:            #check if the height entered is between 1 and 8
        break                       #break out of while loop when if statement is true

for i in range(1, height + 1):      #create for loop and print the height of the pyramid starting at 1
    spaces = " " * (height - i)     #calculate the amount of spaces and store it in the spaces variable
    bricks = '#' * i                #calculate the amount of bricks and store it in the brick variable
    print(spaces + bricks)          #print out the spaces and bricks

