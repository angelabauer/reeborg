from library import*

def build_move_stop():
    if not wall_on_right():
        turn_right()
        build_wall()
        
    elif wall_in_front():
        turn_left()
        
    else:
        move()
move()
turn_right()
move()

while not at_goal():
    build_move_stop()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
def draw_one():
    move()
    put()
    move()
    put()
    move()
    put()
    move()
    put()
    move()
    put()
def draw_zero():
    move()
    put()
    move()
    put()
    move()
    put()
    turn_right()
    move()
    put()
    move()
    put()
    move()
    put()
    move()
    put()
    turn_right()
    move()
    put()
    move()
    put()
    turn_right()
    move()
    put()
    move()
    put()
    move()
    put()
    move()
    
def move_three():
    move()
    move()
    move()
    
    