import random

attempts = 0

number = random.randint(1,10)    

while attempts < 4:
    attempts += 1
    print number       #print number to help with testing
    guess = int(raw_input("Guess a number from 1 to 10: "))
    if guess == number:
        print "you guessed the number!", 
        again = raw_input("do you want to play again? y or n  ")      
        if again == "y":
            number = random.randint(1,10)
            attempts = 0    # gives 4 attempts to a new game
        else:
            print "good bye"                
            break    
    elif attempts == 4:
        print "The game is over!"



        
        
        
    
    
