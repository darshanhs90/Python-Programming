# implementation of card game - Memory

import simplegui
import random
list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5,6,7,8]
exposed=[]
global list
global clickCounter
global prevelement,currelement,prevIndex,currIndex,turns
# helper function to initialize globals
def new_game():
    global list,list1,list2,exposed,turns,clickCounter,prevelement,currelement,prevIndex,currIndex
    turns=0
    prevelement=-1
    currelement=-1
    clickCounter=0
    initelement=-1
    prevIndex=-1
    currIndex=-1
    exposed=[]
    state=0
    for i in range(16):
        exposed.append("False")
    random.shuffle(list1)
    random.shuffle(list2)
    list=list1+list2 
    strin="Turns = "+str(turns)
    label.set_text(strin)
    #print list
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global list,exposed,prevelement,turns,currelement,prevIndex,currIndex,clickCounter
    flag=True
    #clickCounter value=2 check and prev and currelement check
    if clickCounter==2:
        clickCounter=0
        if prevelement!=currelement:
            exposed[prevIndex]="False"
            exposed[currIndex]="False"
        prevelement=currelement=prevIndex=currIndex=-1

    
    for i in range(16):
        x=i*50
        if(pos[0]>=x and pos[0]<x+50):
            if exposed[i]=="True" :
                flag=False
            else:
                index=i
                exposed[i]="True"
            #print list[i]
    if flag==True:
        turns+=1
        clickCounter+=1
        prevelement=currelement
        currelement=list[index]
        prevIndex=currIndex
        currIndex=index
    strin="Turns = "+str(turns)
    label.set_text(strin)
    #print prevelement,currelement,clickCounter
    pass
     
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list,exposed,label
    for i in range(16):
        if(exposed[i]!="False"):
            canvas.draw_text(str(list[i]),[i*50+10,70],40,"White")
        else:
            canvas.draw_polygon([[i*50,0], [i*50+50, 0], [i*50+50,100],[i*50,100]], 2, 'Green')
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric