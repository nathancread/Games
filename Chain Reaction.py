
import pygame
import random
import os
import math
from pygame import *
from tkinter import *
from pygame.locals import *


# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUEISH  = (  12, 237, 207)
GREENISH = (  12, 237, 162)
GREY     = (  51,  46,  40) 
PI = 3.141592653
player_number = 0 
# Set the height and width of the screen
width = 755
height = 1005
size = [width,height]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chain Reaction")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

board_list =  [[0 for ii in range(8)] for jj in range (6)]
Player_list = [[0 for zz in range(8)] for yy in range (6)]




def explode (player_num) :
    
    print (aa)
    print (bb)
    print ("in the explode loop", player_num)
    qq = 1
    while qq == 1 :
        if aa == 0 and bb==0 :
            board_list[aa+1][bb] += 1
            board_list[aa][bb+1] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa][bb+1] = player_num
            Player_list[aa][bb] = 0
            break

        if aa == 0 and bb==7 :
            board_list[aa+1][bb] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb] = 0
            break

        if aa == 5 and bb==0 :
            board_list[aa-1][bb] += 1
            board_list[aa][bb+1] += 1
            board_list[aa][bb] = 0
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb+1] = player_num
            Player_list[aa][bb] = 0
            break

        if aa == 5 and bb==7 :
            board_list[aa-1][bb] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb] = 0           
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb] = 0
            
            break
            
        elif aa == 0 :
            board_list[aa+1][bb] += 1
            board_list[aa][bb+1] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa][bb+1] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb] = 0
            print("working")
            break

        elif aa == 5 :
            board_list[aa][bb+1] += 1
            board_list[aa-1][bb] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb] = 0
            Player_list[aa][bb+1] = player_num
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb] = 0
            print("working")
            break
            
        elif bb == 0 :
            board_list[aa+1][bb] += 1
            board_list[aa][bb+1] += 1
            board_list[aa-1][bb] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa][bb+1] = player_num
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb] = 0
            print("working")
            break

        elif bb == 7 :
            board_list[aa+1][bb] += 1
            board_list[aa-1][bb] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb] = 0
            print("working")
            break


        else :
            board_list[aa+1][bb] += 1
            board_list[aa-1][bb] += 1
            board_list[aa][bb-1] += 1
            board_list[aa][bb+1] += 1
            board_list[aa][bb] = 0
            Player_list[aa+1][bb] = player_num
            Player_list[aa-1][bb] = player_num
            Player_list[aa][bb-1] = player_num
            Player_list[aa][bb+1] = player_num
            Player_list[aa][bb] = 0
            break

        
        
            
        
                

    
    
def draw_screen_function() :
    global board_list 

    screen.fill(WHITE)

    #image = pygame.image.load
    # Draw a rectangle
    if player_number == 0 :
        color = BLUE
    if player_number == 1 :
        color = BLUE
    else :
        color = RED
    for x_offset in range(0, 755, 125):
        pygame.draw.line(screen,color,[0+x_offset,0],[0+x_offset,1005],5)
        
    for y_offset in range(0, 1005, 125):
        pygame.draw.line(screen,color,[0,0+y_offset],[750,0+y_offset],5)
        
    for xx in range(6) :
        for yy in range (8) :
            if (board_list[xx][yy] == 1) and Player_list[xx][yy] == 2 :
               pygame.draw.circle(screen, BLUE, (xx*125+42, yy*125+42), 30, 2)
            if (board_list[xx][yy] == 2) and Player_list[xx][yy] == 2:
                pygame.draw.circle(screen, BLUE, (xx*125+42, yy*125+42), 30, 2)
                pygame.draw.circle(screen, BLUE, (xx*125+82, yy*125+42), 30, 2)
            if (board_list[xx][yy] == 3) and Player_list[xx][yy] == 2 :
                pygame.draw.circle(screen, BLUE, (xx*125+42, yy*125+42), 30, 2)
                pygame.draw.circle(screen, BLUE, (xx*125+82, yy*125+42), 30, 2)
                pygame.draw.circle(screen, BLUE, (xx*125+62, yy*125+72), 30, 2)
                
            if (board_list[xx][yy] == 1) and Player_list[xx][yy] == 1 :
               pygame.draw.circle(screen, RED, (xx*125+42, yy*125+42), 30, 2)
            if (board_list[xx][yy] == 2) and Player_list[xx][yy] == 1:
                pygame.draw.circle(screen, RED, (xx*125+42, yy*125+42), 30, 2)
                pygame.draw.circle(screen, RED, (xx*125+82, yy*125+42), 30, 2)
            if (board_list[xx][yy] == 3) and Player_list[xx][yy] == 1 :
                pygame.draw.circle(screen, RED, (xx*125+42, yy*125+42), 30, 2)
                pygame.draw.circle(screen, RED, (xx*125+82, yy*125+42), 30, 2)
                pygame.draw.circle(screen, RED, (xx*125+62, yy*125+72), 30, 2)
             




draw_screen_function()

#start with player 1
player_number = 2

number_of_times_through = 0


# Loop as long as done == False
while not done:







   
    







 
     # Flag that we are done so we exit this loop

 




    

    #if pygame.event.wait() == pygame.MOUSEBUTTONDOWN:
    #    pos = pygame.mouse.get_pos()
    #    mouse_x = pos[0]
    #    mouse_y = pos[1]    
    #    pygame.draw.circle(screen, BLUE, (mouse_x,mouse_y), 15, 2)

    
    for event in pygame.event.get():   
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            #pygame.draw.circle(screen, BLUE, (mouse_x,mouse_y), 30, 2)
            print (mouse_x,mouse_y)
            box_x = int(mouse_x / 125)
            box_y = int(mouse_y / 125)

            print (box_x, box_y)

            player_number += 1
            if (player_number>2) : player_number = 1
            print ("player number", player_number)

            if ((Player_list[box_x][box_y]!=0) and (Player_list[box_x][box_y]!=player_number)) :
                print ("ERROR- not your box")
                player_number += 1
                if (player_number>2) : player_number = 1
                continue

            Player_list[box_x][box_y] = player_number

            # now that we know which box was picked, increment cicrles and deal with explosions

            board_list[box_x][box_y] += 1

            ## You need to deal with cases where it went over 3 and explodes
            ## on on middle, on 2 for edge, and on 1 for corner.
            explode_check = 0 
            while explode_check != 1 :
                explode_check = 1   
                for aa in range(6) :
                    for bb in range(8) :
                        if ((aa==0 and bb==0) or (aa==5 and bb==7) or (aa==0 and bb==7) or (aa==5 and bb==0)) :
                            if board_list[aa][bb] >= 2 :                               
                                explode (player_number)
                                explode_check = 0
                                
                        elif (aa==0 or aa==5 or bb==0 or bb==7) :
                            if board_list[aa][bb] >= 3 :
                                print("edge")
                                explode (player_number)
                                explode_check = 0
                                
                        else :
                            if board_list[aa][bb] > 3 :
                                print ("mid")
                                explode (player_number)
                                explode_check = 0

                              
            draw_screen_function()

            number_of_times_through += 1
            current_winner=0
            if (number_of_times_through>2) :
                for aa in range(6) :
                    for bb in range(8) :
                        if ((Player_list[aa][bb] != 0) and (current_winner == 0)):
                            current_winner = Player_list[aa][bb]
                        elif ((Player_list[aa][bb] != 0) and (current_winner != Player_list[aa][bb])) :
                            current_winner = 0
                            break
            if (current_winner!=0) : 
                print ("player ", current_winner, " VICTORY")
                break
                




#---------------------------------------------------------------------------------------------------------------------------------------------------
         



                



            
            #else if (box_x==0 || box_x==7 ...) and >2 ## explode edge
            #else if (>3) ## explode inside

            #print (board_list[box_x][box_y])

            ##
            ## ahva a for loop that walks through every box and prints 0, 1, 2 or 3 cicrles
                                


            
           
                



    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
        

