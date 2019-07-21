
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10443606
#    Student name: BONFILIO ALDRINO SUGIARTO
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 4, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 4, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 4, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 4, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#

#*********************************************************#
#***********************DRAWING CARDS*********************#
pen = 'black'
width_card = 120
height_card = 200

def basketball(game):
    # Draw Card's Background
    pencolor(pen)
    width(2)
    pd()
    fillcolor('light blue')
    begin_fill()
    for cards in range(2):
            forward(width_card//2)
            circle(-20,90)
            forward(height_card)
            circle(-20,90)
            forward(width_card//2)
    end_fill()
    pu()
    right(180)
    forward(70)
    left(90)
    forward(35)
    pd()
    write(game + 1, font=("Arial", 25, "bold")) # Drawing the number of the cards. It based on game. Game 
                                                # is the number of card that being drawn.
    pu()
    left(32)
    forward(230)
    pd()
    write(game + 1, font=("Arial", 25, "bold"))
    pu()
    left(147)
    forward(230)

    # Draw The Basketball
    fillcolor('Dark Orange') 
    left(90)
    forward(130)
    left(90)
    forward(100)

    begin_fill()
    pd()
    circle(75)
    end_fill()

    left(90)
    forward(150)

    left(100)
    forward(20)
    left(40)
    forward(10)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(15)
    forward(20)
    left(15)
    forward(20)
    left(10)
    forward(10)
    
    pu()
    left(43)
    forward(35)
    pd()

    setheading(-40)
    forward(10)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(10)
    forward(20)
    left(15)
    forward(20)
    left(15)
    forward(20)
    left(10)
    forward(10)
    pu()
    home()

def tennisball(game):
    # Draw Card's Background
    pencolor(pen)
    width(2)
    pd()
    fillcolor('Snow3')
    begin_fill()
    for cards in range(2):
            forward(width_card//2)
            circle(-20,90)
            forward(height_card)
            circle(-20,90)
            forward(width_card//2)
    end_fill()
    pu()
    right(180)
    forward(70)
    left(90)
    forward(35)
    pd()
    write(game + 1, font=("Arial", 25, "bold")) # Drawing the number of the cards. It based on game. Game 
                                                # is the number of card that being drawn.
    pu()
    left(32)
    forward(230)
    pd()
    write(game + 1, font=("Arial", 25, "bold"))
    pu()
    left(147)
    forward(230)
    
    # Draw The Tennisball
    fillcolor('lawn green') 
    left(90)
    forward(130)
    left(90)
    forward(100)

    begin_fill()
    pd()
    circle(75)
    end_fill()

    pu()
    circle(75,60)
    pd()
    pencolor('snow')
    width(4)
    left(65)
    forward(10)
    left(20)
    forward(15)
    left(20)
    forward(15)
    left(20)
    forward(15)
    left(20)
    forward(15)
    left(20)
    forward(15)
    right(20)
    forward(10)
    right(25)
    forward(10)
    right(25)
    forward(15)
    right(25)
    forward(15)
    right(25)
    forward(15)
    right(20)
    forward(15)
    right(20)
    forward(15)
    right(20)
    forward(15)
    right(25)
    forward(15)
    right(25)
    forward(15)
    left(25)
    forward(15)
    left(25)
    forward(15)
    left(25)
    forward(15)
    left(15)
    forward(4)
    pu()
    pencolor('black')
    width(0)
    home()
        
def bowlingball(game):
    # Draw Card's Background
    pencolor(pen)
    width(2)
    pd()
    fillcolor('Snow3')
    begin_fill()
    for cards in range(2):
            forward(width_card//2)
            circle(-20,90)
            forward(height_card)
            circle(-20,90)
            forward(width_card//2)
    end_fill()
    pu()
    right(180)
    forward(70)
    left(90)
    forward(35)
    pd()
    write(game + 1, font=("Arial", 25, "bold")) # Drawing the number of the cards. It based on game. Game 
                                                # is the number of card that being drawn.
    pu()
    left(32)
    forward(230)
    pd()
    write(game + 1, font=("Arial", 25, "bold"))
    pu()
    left(147)
    forward(230)
    
    #Draw The Bowlingball
    fillcolor('dodger blue') 
    left(90)
    forward(130)
    left(90)
    forward(100)

    begin_fill()
    pd()
    circle(75)
    end_fill()
    pu()

    left(90)
    forward(60)
    left(90)
    forward(20)
    pd()
    dot(20)
    pu()

    right(90)
    forward(30)
    pd()
    dot(20)
    pu()

    right(180)
    forward(15)
    left(90)
    forward(45)
    pd()
    dot(25)
    pu()
    home()
        
def soccerball(game):
    # Draw Card's Background
    pencolor(pen)
    width(2)
    pd()
    fillcolor('Chartreuse')
    begin_fill()
    for cards in range(2):
            forward(width_card//2)
            circle(-20,90)
            forward(height_card)
            circle(-20,90)
            forward(width_card//2)
    end_fill()
    pu()
    right(180)
    forward(70)
    left(90)
    forward(35)
    pd()
    write(game + 1, font=("Arial", 25, "bold")) # Drawing the number of the cards. It based on game. Game 
                                                # is the number of card that being drawn.
    pu()
    left(32)
    forward(230)
    pd()
    write(game + 1, font=("Arial", 25, "bold"))
    pu()
    left(147)
    forward(230)
    
    #Draw The Soccerball
    fillcolor('ghost white') 
    left(90)
    forward(130)
    left(90)
    forward(100)

    begin_fill()
    pd()
    circle(75)
    end_fill()
    pu()

    circle(75,35)

    pd()
    fillcolor('black')
    begin_fill()
    left(93)
    forward(18)
    right(75)
    forward(45)
    right(80)
    forward(15)
    right(70)
    circle(-50,48)
    end_fill()
    right(48)
    forward(35)
    left(40)
    forward(20)

    begin_fill()
    left(65)
    forward(20)
    right(85)
    circle(-52,60)
    right(75)
    forward(18)
    end_fill()

    left(45)
    forward(20)
    left(45)
    forward(22)

    begin_fill()
    left(60)
    forward(17)
    right(93)
    circle(-55,63)
    right(90)
    forward(18)
    end_fill()

    left(50)
    forward(20)
    left(50)
    forward(20)

    begin_fill()
    left(70)
    forward(22)
    right(93)
    circle(-55,63)
    right(90)
    forward(20)
    end_fill()

    left(65)
    forward(15)
    left(45)
    forward(15)

    begin_fill()
    left(70)
    forward(20)
    right(100)
    circle(-53,50)
    right(90)
    forward(15)
    end_fill()

    left(45)
    forward(15)
    left(90)
    forward(20)

    right(180)
    forward(20)
    left(45)
    forward(20)
    
    begin_fill()
    left(60)
    forward(25)
    right(80)
    forward(30)
    right(70)
    forward(30)
    right(73)
    forward(28)
    right(77)
    forward(28)
    end_fill()

    right(180)
    forward(25)
    right(75)
    forward(17)

    right(180)
    forward(17)
    right(35)
    forward(30)
    right(53)
    forward(15)

    right(180)
    forward(15)
    right(45)
    forward(32)
    right(71)
    forward(25)
    right(180)
    forward(25)
    right(40)
    forward(30)
    right(60)
    forward(25)
    pu()
    home()

def joker():
    # Draw Card's Background
    pencolor(pen)
    width(2)
    pd()
    fillcolor('firebrick')
    begin_fill()
    for cards in range(2):
            forward(width_card//2)
            circle(-20,90)
            forward(height_card)
            circle(-20,90)
            forward(width_card//2)
    end_fill()
    pu()

    # Draw The Baseball Bat as The Joker

    right(180)
    forward(75)
    left(90)
    forward(220)
    left(48)
    forward(10)
    pd()

    fillcolor('white')
    begin_fill()
    forward(5)
    left(35)
    forward(5)
    left(25)
    forward(5)
    left(25)
    forward(5)
    left(35)
    forward(5)
    left(35)
    forward(5)
    left(25)
    forward(15)
    left(35)
    forward(5)
    left(35)
    forward(5)
    left(15)
    forward(5)
    left(25)
    forward(5)
    left(35)
    forward(5)
    left(35)
    forward(9)
    end_fill()

    pu()
    left(80)
    forward(15)
    left(21)
    pd()
    pencolor('black')
    fillcolor('black')
    begin_fill()
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(40)
    forward(2)
    left(60)
    forward(2)
    left(35)
    forward(2)
    left(15)
    forward(2)
    left(15)
    forward(2)
    left(10)
    forward(3)
    left(15)
    forward(2)
    left(35)
    forward(2)
    left(15)
    forward(2)
    left(25)
    forward(2)
    end_fill()

    pu()
    pencolor('black')
    fillcolor('white')
    begin_fill()
    right(4.5)
    forward(100)
    #pencolor(pen)
    pd()
    forward(50)
    right(20)
    forward(25)
    left(20)
    forward(60)
    left(90)

    right(60)
    forward(2)
    left(40)
    forward(5)
    left(20)
    forward(9)
    left(10)
    forward(5)
    left(5)
    forward(5)
    left(20)
    forward(3)
    left(20)
    forward(3)
    left(35)
    forward(55)
    left(20)
    forward(25)
    right(20)
    forward(52)
    left(90)
    forward(12)
    end_fill()
    pu()
    home()

#*********************************************************#
#*********************CARD'S FUNCTION*********************#

# Draw the card stacks as per the provided game specification
def deal_cards(game_type):                          
    position = [Vec2D(-449, 350), Vec2D(-270, 350), 
                Vec2D(-91, 350), Vec2D(88, 350),    
                Vec2D(267, 350), Vec2D(446, 350)]   
    offset = Vec2D(0, -50)                          

    for all_elements in game_type:                  
        for game in range(all_elements[2]):         
            if all_elements[0] == 'Stack 1':       
                goto(position[0])                   
                if game + 1 == all_elements[3]:     
                    joker()                         
                elif all_elements[1] == 'Suit A':   
                    basketball(game)                
                elif all_elements[1] == 'Suit B':  
                    tennisball(game)               
                elif all_elements[1] == 'Suit C':   
                    bowlingball(game)               
                else:                               
                    soccerball(game)                
                position[0] += offset               

            if all_elements[0] == 'Stack 2':        
                goto(position[1])                   
                if game + 1 == all_elements[3]:
                    joker()
                elif all_elements[1] == 'Suit A':
                    basketball(game)
                elif all_elements[1] == 'Suit B':
                    tennisball(game)
                elif all_elements[1] == 'Suit C':
                    bowlingball(game)
                else:
                    soccerball(game)
                position[1] += offset    

            if all_elements[0] == 'Stack 3':        
                goto(position[2])
                if game + 1 == all_elements[3]:
                    joker()
                elif all_elements[1] == 'Suit A':
                    basketball(game)
                elif all_elements[1] == 'Suit B':
                    tennisball(game)
                elif all_elements[1] == 'Suit C':
                    bowlingball(game)
                else:
                    soccerball(game)
                position[2] += offset
                
            if all_elements[0] == 'Stack 4':        
                goto(position[3])
                if game + 1== all_elements[3]:
                    joker()
                elif all_elements[1] == 'Suit A':
                    basketball(game)
                elif all_elements[1] == 'Suit B':
                    tennisball(game)
                elif all_elements[1] == 'Suit C':
                    bowlingball(game)
                else:
                    soccerball(game)
                position[3] += offset
                
            if all_elements[0] == 'Stack 5':        
                goto(position[4])
                if game + 1 == all_elements[3]:
                    joker()
                elif all_elements[1] == 'Suit A':
                    basketball(game)
                elif all_elements[1] == 'Suit B':
                    tennisball(game)
                elif all_elements[1] == 'Suit C':
                    bowlingball(game)
                else:
                    soccerball(game)
                position[4] += offset
                
            if all_elements[0] == 'Stack 6':        
                goto(position[5])
                if game + 1 == all_elements[3]:
                    joker()
                elif all_elements[1] == 'Suit A':
                    basketball(game) 
                elif all_elements[1] == 'Suit B':
                    tennisball(game)
                elif all_elements[1] == 'Suit C':
                    bowlingball(game) 
                else: 
                    soccerball(game)
                position[5] += offset               


        

        


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Patience")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_3) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

