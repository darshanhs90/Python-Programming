# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random 

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":   
        return 1
    elif name=="paper":   
         return 2
    elif name=="lizard":   
         return 3
    else:   
         return 4
    
def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:   
        return "Spock"
    elif number==2:   
        return "paper"
    elif number==3:   
        return "lizard"
    else:   
        return "scissors"
 
def rpsls(player_choice): 
    print ""
    print "Player chooses",player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(1,5)
    computer_choice=number_to_name(comp_number)
    print "Computer chooses",computer_choice
    diff= (-comp_number+player_number)%5
    if diff==0:
        print "Player and computer tie!"
    elif diff>2:
       print "Computer wins!"
    else:
       print "Player wins!"
   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


