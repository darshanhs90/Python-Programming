# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
dealqn=""
score = 0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
global player_hand,dealer_hand,lst,d
busted=False

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list=[]# empty list of cards
        pass	# create Hand object

    def __str__(self):
        s="Hand Contains "
        for i in range(len(self.list)):
            s+=str(self.list[i])+" "
        return s
        pass	# return a string representation of a hand

    def add_card(self, card):
        #print "add card"
        self.list.append(card)#append card to the list
        pass	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        aceCount=0
        val=0
        for i in range(0,len(self.list)):
            st=str(self.list[i])
            st=st.replace('C',"")
            st=st.replace('S',"")
            st=st.replace('H',"")
            st=st.replace('D',"")
            val+=VALUES[st]
            if(val==1):
                aceCount+=1
        #print val    
        for i in range(0,aceCount):
            if(val<11):
                val=val+10
        
        return val
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.list)):
            
            st=str(self.list[i])
            st1=str(self.list[i])
            st=st.replace('C',"")
            st=st.replace('S',"")
            st=st.replace('H',"")
            st=st.replace('D',"")
            val=RANKS.index(st)
            val1= st1.partition(st)[0]
            val2=SUITS.index(val1)
            if(pos[1]!=200):
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * val, 
                            CARD_CENTER[1] + CARD_SIZE[1] * val2)
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]+i*CARD_SIZE[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            else:
                if(in_play==True):
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * val, 
                            CARD_CENTER[1] + CARD_SIZE[1] * val2) 
                    if(i==0):
                        if(val2==2 or val2==3):#red colour
                             card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0] * 1, 
                                     CARD_BACK_CENTER[1] )
                   
                        else:#black colour
                              card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1] )      
                        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]+i*CARD_SIZE[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    else:
                        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]+i*CARD_SIZE[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                else:
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * val, 
                            CARD_CENTER[1] + CARD_SIZE[1] * val2)
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]+i*CARD_SIZE[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
          
        pass	# draw a hand on the canvas, use the draw method for cards
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.list=[]
        for i in range(0,len(SUITS)):
            for j in range(0,len(RANKS)):
             self.list.append(str((SUITS[i]+RANKS[j])))
        
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.list)
       # print "shuffle"
        pass    # use random.shuffle() 

    def deal_card(self):
        r=random.randrange(0,len(self.list))
       # print self.list[r]
        return self.list[r]
        
        pass	# deal a card object from the deck
    
    def __str__(self):
        s=""
        for i in range(len(self.list)):
            s+=self.list[i]+" "
        return s
        
        pass	# return a string representing the deck
        
 


#define event handlers for buttons
def deal():
    global outcome,dealqn,in_play,player_hand,dealer_hand,lst,d,score
    outcome=""
    if(in_play==True):
        in_play=False
        outcome="Dealer Wins"
        dealqn="New Deal?"
        score-=1
    else:
        d=Deck()
        d.shuffle()
    # your code goes here
        lst=[]
        for i in range(0,4):
            x= d.deal_card()
            while x in lst:
                x=d.deal_card()
            lst.append(x)
            dealqn="Hit or Stand?"
        player_hand=Hand()
        dealer_hand=Hand()
        player_hand.add_card(lst[0])
        player_hand.add_card(lst[1])
        dealer_hand.add_card(lst[2])
        dealer_hand.add_card(lst[3])
        #print "Player "+str(player_hand)
        #print "Dealer "+str(dealer_hand)
        player_hand.get_value()
        in_play = True
    
def hit():
    pass	# replace with your code below
    global lst,player_hand,dealqn,d,busted,outcome,score,in_play
    # if the hand is in play, hit the player
    busted=False
    if(in_play==True):
        if(player_hand.get_value()<21):
            x=d.deal_card()
            while x in lst:
                x=d.deal_card()
            player_hand.add_card(x)
            lst.append(x)
        if(player_hand.get_value()==21):
            stand()
        if(player_hand.get_value()>21):
            #print "Player is Busted"
            outcome="Dealer Wins,Player is Busted"
            dealqn="New Deal?"
            score-=1
            busted=True
            in_play=False
        #in_play=False
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global busted,dealer_hand,dealqn,lst,outcome,score,in_play
    pass	# replace with your code below
    if(in_play==True):
        if(busted==True):
            #print "Player is busted"
            in_play=False
            dealqn="New Deal?"
        else:
            in_play=False
            while(dealer_hand.get_value()<17):
                x=d.deal_card()
                while x in lst:
                     x=d.deal_card() 
                dealer_hand.add_card(x)
            if(dealer_hand.get_value()>21):
                #print "Dealer is Busted"
                outcome="Player Wins,Dealer is Busted"
                dealqn="New Deal?"
                score+=1
            elif(player_hand.get_value()>dealer_hand.get_value()):
                #print "player wins"
                dealqn="New Deal?"
                outcome="Player Wins"
                score=score+1
            else:
                #print "Dealer wins"
                outcome="Dealer Wins"
                dealqn="New Deal?"
                score=score-1
            #deal()
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('BLACKJACK', (100, 100), 45, 'Cyan')
    canvas.draw_text('Score : '+str(score), (450, 100), 20, 'Black')
    canvas.draw_text('Dealer ', (100, 200), 20, 'Black')
    canvas.draw_text('Player ', (100, 400), 20, 'Black')
    canvas.draw_text(dealqn, (350, 400), 20, 'Black')
    canvas.draw_text(outcome, (300, 200), 20, 'White')
    player_hand.draw(canvas, [100, 405])
    dealer_hand.draw(canvas, [100, 205])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric