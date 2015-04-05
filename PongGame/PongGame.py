# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[0,0]
ball_vel=[0,0]
paddle1_pos=PAD_HEIGHT/2
paddle2_pos=PAD_HEIGHT/2
paddle1_vel=0
paddle2_vel=0
left_score=0
right_score=0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global WIDTH,HEIGHT
    ball_pos=[WIDTH/2,HEIGHT/2]    
    h=random.randrange(2,5)
    v=random.randrange(2,5)
    #print direction
    if direction=="RIGHT":
        ball_vel=[h,-v]
    else:
        ball_vel=[-h,-v]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global left_score,right_score
    left_score=0
    right_score=0
    spawn_ball("LEFT")
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel,left_score,right_score
   # draw mid line and gutters
    canvas.draw_text(str(left_score),[WIDTH/2+25,HEIGHT/2-100],25,"WHITE")
    canvas.draw_text(str(right_score),[WIDTH/2-40,HEIGHT/2-100],25,"WHITE")
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if ball_pos[1]>HEIGHT-BALL_RADIUS-1:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]<BALL_RADIUS+1:
        ball_vel[1]=-ball_vel[1]    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,"WHITE")
    # update paddle's vertical position, keep paddle on the screen
    if HEIGHT/2-paddle1_pos+paddle1_vel<0:
        paddle1_vel=paddle1_vel+20
    elif HEIGHT/2+paddle1_pos+paddle1_vel>HEIGHT:
        paddle1_vel=paddle1_vel-20
    
    if HEIGHT/2-paddle2_pos+paddle2_vel<0:
        paddle2_vel=paddle2_vel+20
    elif HEIGHT/2+paddle2_pos+paddle2_vel>HEIGHT:
        paddle2_vel=paddle2_vel-20    
    
    if  ball_pos[0]+BALL_RADIUS-(WIDTH-PAD_WIDTH+1)>=-9 and  ball_pos[0]+BALL_RADIUS-(WIDTH-PAD_WIDTH+1)<=5:
        #if ball_pos[1] is within the paddle height then rebound or else respawn
        #right extreme
        if ball_pos[1]>HEIGHT/2-paddle2_pos+paddle2_vel and ball_pos[1]<HEIGHT/2+paddle2_pos+paddle2_vel:
            ball_vel[0]=-1.1*ball_vel[0] 
        else:
            right_score+=1
            spawn_ball("LEFT") 
    if ball_pos[0]-BALL_RADIUS-(PAD_WIDTH+1)<5 and ball_pos[0]-BALL_RADIUS-(PAD_WIDTH+1)>=-5:
        #if ball_pos[1] is within the paddle height then rebound or else respawn
        #left extreme
        if ball_pos[1]>HEIGHT/2-paddle1_pos+paddle1_vel and ball_pos[1]<HEIGHT/2+paddle1_pos+paddle1_vel:
            ball_vel[0]=-1.1*ball_vel[0] 
        else:
            left_score+=1
            spawn_ball("RIGHT")
    #print ball_vel
    if ball_pos[0]+BALL_RADIUS>(WIDTH-PAD_WIDTH+10):
        spawn_ball("RIGHT")
    if ball_pos[0]-BALL_RADIUS<(PAD_WIDTH-5):
        spawn_ball("LEFT") 
    
    # draw paddles	
    canvas.draw_polygon([(0,HEIGHT/2-paddle1_pos+paddle1_vel),(PAD_WIDTH,HEIGHT/2-paddle1_pos+paddle1_vel),(PAD_WIDTH,HEIGHT/2+paddle1_pos+paddle1_vel),(0,HEIGHT/2+paddle1_pos+paddle1_vel)],1,"WHITE")
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,HEIGHT/2-paddle2_pos+paddle2_vel),(WIDTH,HEIGHT/2-paddle2_pos+paddle2_vel),(WIDTH,HEIGHT/2+paddle2_pos+paddle2_vel),(WIDTH-PAD_WIDTH,HEIGHT/2+paddle2_pos+paddle2_vel)],1,"WHITE")
    
    # draw scores
    #canvas.draw_scores(0)    
def keydown(key):
    global paddle1_vel, paddle2_vel
    #print chr(key)
    if chr(key)=='S':
        paddle1_vel+=20
    elif chr(key)=='W':
        paddle1_vel+=-20
    elif chr(key)=='(':
        paddle2_vel+=20
    elif chr(key)=='&':
        paddle2_vel+=-20
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel

def button_handler():
   new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('RESTART', button_handler)


# start frame
new_game()
frame.start()
