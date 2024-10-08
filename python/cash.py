from cs50 import get_float                    #import the cs50 library to use get_float

coins = [25, 10, 5, 1]                          #declare a list of the coins
coin_count = 0                                  #initialize a counter to equal zero

while True:                                     #create a while loop
    change = get_float("Change owed: ")         #prompt the user to enter change owed
    if change > 0:                              #check if the change entered is not less than zero, meaning its bigger than 0
        break                                   #break out of the loop when the if statement returns as true

change = int(change * 100)                            #convert the change from dollars to cents by multiplying by 100

for i in range(len(coins)):                           #loop through the length of the list of coins checking each one

     coin_count = coin_count + change // coins[i]     #get the amount of coins from the change then add it to the counter ,using integer division
     change = change % coins[i]                       #calculate what is left of the change and update the change variable

print(coin_count)                                     #print out the amount of coins
