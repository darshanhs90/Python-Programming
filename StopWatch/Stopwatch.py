# template for "Stopwatch: The Game"
import simplegui
# define global variables
count=0
success=0
tries=0
watch_run=False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t<10:
        return "0:00:"+str(t)
    elif t<100:
        z=t/10
        z1=t%10
        return "0:0"+str(z)+":"+str(z1)
    elif t<600:
        z2=t%10
        t=t/10
        z1=t%10
        z=t/10
        return "0:"+str(z)+str(z1)+":"+str(z2)
    else:
        z4=t/600
        t=t-(600*z4)
        z2=t%10
        t=t/10
        z1=t%10
        z=t/10
        return str(z4)+":"+str(z)+str(z1)+":"+str(z2)
    return "0"
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global watch_run
    timer.start()
    watch_run=True
def stop():
    global watch_run
    if watch_run:
        global count
        timer.stop()
        global tries
        global success
        tries=tries+1
        new_string=format(count)
        if count>0 and new_string[-1]=="0":
           success=success+1 
        watch_run=False
def reset():
    timer.stop()
    global count,success,tries
    count=0   
    tries=0
    success=0
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count=count+1
# define draw handler
def draw(canvas):
    global count  
    global success
    global tries
    new_string=format(count)
    canvas.draw_text(new_string,[130,150],24,"White")    
    canvas.draw_text(str(success)+"/"+str(tries),[250,20],20,"Green")
   
# create frame
frame=simplegui.create_frame("Stopwatch: The Game",300,300)

# register event handlers
frame.add_button("Start",start,80)
frame.add_button("Stop",stop,80)
frame.add_button("Reset",reset,80)
timer=simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)
# start frame
frame.start()
# Please remember to review the grading rubric
