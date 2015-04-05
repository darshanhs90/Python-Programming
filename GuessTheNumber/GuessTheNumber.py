# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
count=7
range=100
secret_number=0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0,range)
    print ""
    print "New game, Range is from 0 to",range
    print "Number of remaining guesses is",count
        
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    global count
    count=7
    range=100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    global count
    count=10
    range=1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    
    global count
    count=count-1
    x = (int)(guess)
    print""
    print "Guess was",x
    print "Number of remaining guesses is",count
    global secret_number
    #print secret_number
    if x<secret_number:
        if count==0:
            print "You Lose,The correct answer was",secret_number
            print ""
        else:
            print "Higher"
    elif x>secret_number:
        if count==0:
            print "You Lose,The correct answer was",secret_number
            print ""
        else:
            print "Lower"
    else:
        print "Correct" 
        if range==100:
                range100()
        else :
                range1000()
    if count==0:
            if range==100:
                range100()
            else :
                range1000()
                
    
        
    # remove this when you add your code
  

    
# create frame
frame=simplegui.create_frame("Guess the number",200,200)
frame.add_button("Range is [0-100)",range100,200)
frame.add_button("Range is [0-1000)",range1000,200)
frame.add_input("Enter a guess",input_guess,200)


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
