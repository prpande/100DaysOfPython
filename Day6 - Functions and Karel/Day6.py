# Dummy function mocks for Reeborg's world
def turn_left():
    pass
def move():
    pass
def wall_in_front():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def wall_on_right():
    pass
def right_is_clear():
    pass

# Practice 1 - Reeborg's Hurdle1 Jumping Challenge

# To be run in Reeborg's world console
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0,6):
    move()
    jump()

# Practice 2 - - Reeborg's Hurdles3 Challenge using While Loops

# To be run in Reeborg's world console
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while (not at_goal()):
    if front_is_clear():
        move()
    else:
        jump()

##

# Practice 3 - Reeborg's Hurdles 4 Challenge with variable heights

# To be run in Reeborg's world console
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while (not at_goal()):
    if front_is_clear():
        move()
    else:
        jump()

##

# Project 6  - Reebog's Escaping the Maze 

## Soln 1
#Simple solution but buggy -> infinite loop in open space
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while (not at_goal()):
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

##

# Soln 2
# Maintains the right wall follow rule
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while (not at_goal()):
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

##


# Soln 3
# Doesnt follow right wall rule but simplest
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while (not at_goal()):
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()    
    else:
        turn_left()

##