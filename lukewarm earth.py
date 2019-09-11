import pygame
import random
import os
import math
#---*-*-*-*-*SEPERATE GRAPHICS PROGRAM-*-*-*-*-*-*-*
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 43,   23,  13)
BLUE     = ( 0,     0,  225)
ORANGE   = (250, 133,  0)
pygame.init()
#bottom is actually side 
BOTTOM = 900
#side is acually bottom
SIDE = 1500

TANK_HEIGTH = 40
TANK_WIDTH  = 80

#PICK_ONE = random.randint(BOTTOM/2,BOTTOM*.8)
#PICK_TWO = random.randint(BOTTOM/2,BOTTOM*4/5)

WIND = random.randint(-5,5)

# Set the width and height of the screen [width, height]
size = (SIDE, BOTTOM)

one_x_upper_left_loc = 300
two_x_upper_left_loc = 900
one_y_upper_left_loc = 0
two_y_upper_left_loc = 0
one_y_lower_left_loc = 0
two_y_lower_left_loc = 0

## Initialize these for now
one_barrel_angle = 20
two_barrel_angle = 20
slope_one = 0
slope_two = 0


one_power = 150
two_power = 20

one_x_angle = math.cos(one_barrel_angle/180*math.pi)
one_y_angle = math.sin(one_barrel_angle/180*math.pi)
two_x_angle = math.cos(two_barrel_angle/180*math.pi)
two_y_angle = math.sin(two_barrel_angle/180*math.pi)


##FIXME: check that power is between 0..100, and angle is between 0..90

screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("lukewarm earth")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
dirt_list =  [[0 for ii in range(BOTTOM)] for jj in range (SIDE)]

first_time_draw = 1
player_one_turn = 1

def print_screen() :
    global dirt_list
    global one_x_upper_left_loc
    global two_x_upper_left_loc
    global one_y_upper_left_loc
    global two_y_upper_left_loc
    global one_y_lower_left_loc
    global two_y_lower_left_loc
    global TANK_HEIGTH
    global TANK_WIDTH
    global slope_one
    global slope_two


    point_array = [0,750 , 120,500 , 500,250 , 750,0 , 1000,333 ,  1200,300 , 1500,12]
    dirt_list =  [[0 for ii in range(BOTTOM)] for jj in range (SIDE)]
    for x in range(SIDE):
        y_is_done = 0
        for y in range (BOTTOM):
            for point_array_index in range(len(point_array)-2)[::2] :
                if x <= point_array[point_array_index+2] and x >= point_array[point_array_index] :
                    if y >= point_array[point_array_index+3] or y >= point_array[point_array_index+1] :
                        m = (point_array[point_array_index+3] - point_array[point_array_index+1])/(point_array[point_array_index+2] - point_array[point_array_index+0])
                        b = (m * point_array[point_array_index+0])- point_array[point_array_index+1]
                        if y >= m * x - b :
                            dirt_list[x][y] = 1
                            screen.set_at((x, y), BROWN)

                            #place tank 
                            if x == one_x_upper_left_loc :
                                one_y_upper_left_loc = y
                                print(one_x_upper_left_loc,one_y_upper_left_loc)
                                print(dirt_list[one_x_upper_left_loc][one_y_upper_left_loc])
                                slope_one = m

                            if x == two_x_upper_left_loc :
                                two_y_upper_left_loc = y
                                slope_two = m

                            
                            #tray- temp
                            for yy in range (y, BOTTOM) :
                                dirt_list[x][yy] = 1
                                screen.set_at((x, yy), BROWN)
                            y_is_done = 1

            if y_is_done : break

                    
    #pygame.display.flip()
    one_y_lower_left_loc = one_y_upper_left_loc - TANK_HEIGTH
    two_y_lower_left_loc = two_y_upper_left_loc - TANK_HEIGTH

def print_tanks() :
    
    #Tank Bodies and barrels
    if slope_one >= 0 :
        pygame.draw.rect(screen, BLUE, [one_x_upper_left_loc, one_y_upper_left_loc, TANK_WIDTH, TANK_HEIGTH], 6)
        pygame.draw.line(screen, WHITE, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc+.2*TANK_HEIGTH],
            [one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc+.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
        print("ayy")
    elif slope_one <= 0 :
        pygame.draw.rect(screen, BLUE, [one_x_upper_left_loc-TANK_WIDTH+15, one_y_lower_left_loc, TANK_WIDTH-15, TANK_HEIGTH], 6)
        pygame.draw.line(screen, WHITE, [one_x_upper_left_loc, one_y_lower_left_loc+.2*TANK_HEIGTH],
            [one_x_upper_left_loc+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
        print("aww")
    if slope_two >= 0 :
        pygame.draw.rect(screen, RED , [two_x_upper_left_loc, two_y_lower_left_loc , TANK_WIDTH, TANK_HEIGTH], 6)
        ###messing around
        pygame.draw.line(screen, WHITE, [two_x_upper_left_loc, two_y_lower_left_loc+.2*TANK_HEIGTH],
            [(two_x_upper_left_loc-(two_x_angle*.5*TANK_WIDTH)), two_y_lower_left_loc+.2*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)], 6)
        ## here
    elif slope_two <= 0 :
        pygame.draw.rect(screen, RED , [two_x_upper_left_loc-TANK_WIDTH+15, two_y_lower_left_loc - TANK_HEIGTH , TANK_WIDTH, TANK_HEIGTH], 6)
    #Tank Barrels
    #pygame.draw.line(screen, BLUE, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc-.8*TANK_HEIGTH],
        #[one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
    #pygame.draw.line(screen, RED , [two_x_upper_left_loc,            two_y_lower_left_loc-.8*TANK_HEIGTH],
       #[two_x_upper_left_loc-two_x_angle*.5*TANK_WIDTH, two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)], 6)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(ORANGE)

    one_x_angle = 0
    


    print_screen()
   
    
    
    #text
    
   

    #black line
    pygame.draw.line(screen, BLACK, [SIDE/2 , BOTTOM], [SIDE/2, 0], 6)


    if first_time_draw:
        print ("Are you ready for WAR!!!")
        print("the wind is ", WIND)
        first_time_draw = 0
        one_barrel_angle = 45
        two_barrel_angle = 45

        one_power = 150
        two_power = 150
        one_x_angle = math.cos(one_barrel_angle/180*math.pi)
        one_y_angle = math.sin(one_barrel_angle/180*math.pi)
        two_x_angle = math.cos(two_barrel_angle/180*math.pi)
        two_y_angle = math.sin(two_barrel_angle/180*math.pi)
        print_tanks()
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 


    elif player_one_turn:
        one_barrel_angle = int(input("enter PLAYER 1 angle: "))


        one_power = 150
        
        one_power = int(input("enter PLAYER 1 power: "))
        
        one_x_angle = math.cos(one_barrel_angle/180*math.pi)
        one_y_angle = math.sin(one_barrel_angle/180*math.pi)

        #pygame.draw.line(screen, BLUE, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc-.8*TANK_HEIGTH],
        #[one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
        #pygame.draw.line(screen, RED , [two_x_upper_left_loc,            two_y_lower_left_loc-.8*TANK_HEIGTH],
        #[two_x_upper_left_loc-two_x_angle*.5*TANK_WIDTH, two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)], 6)

        #Tank Bodies and barrels
        if slope_one >= 0 :
            pygame.draw.rect(screen, BLUE, [one_x_upper_left_loc, one_y_lower_left_loc, TANK_WIDTH, TANK_HEIGTH], 6)
            pygame.draw.line(screen, BLACK, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc+.2*TANK_HEIGTH],
                [one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*(.5*TANK_WIDTH)), one_y_lower_left_loc+.2*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
            print("AHHHH")
        elif slope_one <= 0 :
            pygame.draw.rect(screen, BLUE, [one_x_upper_left_loc-TANK_WIDTH+15, one_y_lower_left_loc - TANK_HEIGTH, TANK_WIDTH, TANK_HEIGTH], 6)
            pygame.draw.line(screen, BLACK, [one_x_upper_left_loc+15, one_y_lower_left_loc-.8*TANK_HEIGTH],
                [one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*(.5*TANK_WIDTH)), one_y_lower_left_loc-.8*TANK_HEIGHT(one_y_angle*.5*TANK_HEIGTH)], 6)
            print("oops")
        if slope_two >= 0 :
            pygame.draw.rect(screen, RED , [two_x_upper_left_loc, two_y_lower_left_loc , TANK_WIDTH, TANK_HEIGTH], 6)
        elif slope_two <= 0 :
            pygame.draw.rect(screen, RED , [two_x_upper_left_loc-TANK_WIDTH+15, two_y_lower_left_loc - TANK_HEIGTH , TANK_WIDTH, TANK_HEIGTH], 6)

        #Tank Barrels
        #pygame.draw.line(screen, BLUE, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc-.8*TANK_HEIGTH],
            #[one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
        #pygame.draw.line(screen, RED , [two_x_upper_left_loc,            two_y_lower_left_loc-.8*TANK_HEIGTH],
            #[two_x_upper_left_loc-two_x_angle*.5*TANK_WIDTH, two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)], 6)

        # Draw player one shot
        x = one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH)
        y = one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)
        hit_dirt = False
        t = .001
        while not hit_dirt:

            x = (one_power * one_x_angle + WIND)*t + one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH)
            y = ((10*t*t) - (one_power * one_y_angle * t) + (one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)))
            t += .25
            x = int(round(x,0))
            y = int(round(y,0))


            #print("Wind is :", WIND, "power is :", one_power, "angle multiplier is : ", math.cos(one_barrel_angle/180*math.pi))
            #print(x)
     
            pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)


            if dirt_list[int(x)][int(y)] == 1 :
                hit_dirt = True

            #if (t>8):
            


        pygame.draw.circle(screen, ORANGE,[int(x),int(y)],30)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        player_one_turn = 0


 


    elif player_one_turn == 0:
        two_barrel_angle = int(input("enter PLAYER 2 angle: "))

        two_power = int(input("enter PLAYER 2 power: "))

        two_x_angle = math.cos(two_barrel_angle/180*math.pi)
        two_y_angle = math.sin(two_barrel_angle/180*math.pi)

        #Tank Barrels
        pygame.draw.line(screen, BLUE, [one_x_upper_left_loc+TANK_WIDTH, one_y_lower_left_loc-.8*TANK_HEIGTH],
        [one_x_upper_left_loc+TANK_WIDTH+(one_x_angle*.5*TANK_WIDTH), one_y_lower_left_loc-.8*TANK_HEIGTH-(one_y_angle*.5*TANK_WIDTH)], 6)
        pygame.draw.line(screen, RED , [two_x_upper_left_loc,            two_y_lower_left_loc-.8*TANK_HEIGTH],
        [two_x_upper_left_loc-two_x_angle*.5*TANK_WIDTH, two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)], 6)

       
        # Draw player two shot
        x = two_x_upper_left_loc-(two_x_angle*.5*TANK_WIDTH)
        y = two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)
        hit_dirt = False
        t = .001
        while not hit_dirt:

            x = -1 * (two_power * two_x_angle + WIND)*t + two_x_upper_left_loc-(two_x_angle*.5*TANK_WIDTH)
            y = ((10*t*t) - (two_power * two_y_angle * t) + (two_y_lower_left_loc-.8*TANK_HEIGTH-(two_y_angle*.5*TANK_WIDTH)))
            t += .25

            #print("Wind is :", WIND, "power is :", two_power, "angle multiplier is : ", math.cos(two_barrel_angle/180*math.pi))
            #print(x)
     
            pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

            #if (t>8):
            x = int(round(x,0))
            y = int(round(y,0))

            if dirt_list[int(x)][int(y)] == 1 :
                hit_dirt = True
     
         

        pygame.draw.circle(screen, ORANGE,[int(x),int(y)],30)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        player_one_turn = 1



 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
#pick - to dirt
