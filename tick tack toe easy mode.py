#keep it running
import os 
import random
print("welcome to TICK-TACK-TOE!!!!!!!!!!")
print("prepare for domination")

#made the list 1-9
tic_tac_list = ['E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game_over = 0
one_is_empty = 0


#game over possibilities, changes vaariable game_over to 1 or 2

def check_if_game_over() :
    global game_over
    if tic_tac_list[7] == 'X' and tic_tac_list[8] == 'X' and tic_tac_list[9] == 'X' : game_over = 1
    if tic_tac_list[4:7] == ['X', 'X', 'X'] : game_over = 1
    if tic_tac_list[1:4] == ['X', 'X', 'X'] : game_over = 1
    if tic_tac_list[1] == 'X' and tic_tac_list[4] == 'X' and tic_tac_list[7] == 'X' : game_over = 1
    if tic_tac_list[2] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[8] == 'X' : game_over = 1
    if tic_tac_list[3] == 'X' and tic_tac_list[6] == 'X' and tic_tac_list[9] == 'X' : game_over = 1
    if tic_tac_list[1] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[9] == 'X' : game_over = 1
    if tic_tac_list[3] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[7] == 'X' : game_over = 1
    
    if tic_tac_list[7] == 'O' and tic_tac_list[8] == 'O' and tic_tac_list[9] == 'O' : game_over = 2
    if tic_tac_list[4:7] == ['O', 'O', 'O'] : game_over = 2
    if tic_tac_list[1:4] == ['O', 'O', 'O'] : game_over = 2
    if tic_tac_list[1] == 'O' and tic_tac_list[4] == 'O' and tic_tac_list[7] == 'O' : game_over = 2
    if tic_tac_list[2] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[8] == 'O' : game_over = 2
    if tic_tac_list[3] == 'O' and tic_tac_list[6] == 'O' and tic_tac_list[9] == 'O' : game_over = 2
    if tic_tac_list[1] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[9] == 'O' : game_over = 2
    if tic_tac_list[3] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[7] == 'O' : game_over = 2

def smart_pick() :
    global one_is_empty

    one_is_empty = 0
    #print("smart_pick: one is empty",one_is_empty)    
    if tic_tac_list[1] == 'O' and tic_tac_list[4] == 'O' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[2] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[8] == ' ' :
        tic_tac_list[8] = 'O'
    elif tic_tac_list[3] == 'O' and tic_tac_list[6] == 'O' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[1] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[3] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[7] == 'O' and tic_tac_list[8] == 'O' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[1] == 'O' and tic_tac_list[2] == 'O' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[4] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[6] == ' ' :
        tic_tac_list[6] = 'O'
    elif tic_tac_list[1] == 'O' and tic_tac_list[7] == 'O' and tic_tac_list[4] == ' ' :
        tic_tac_list[4] = 'O'
    elif tic_tac_list[2] == 'O' and tic_tac_list[8] == 'O' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[3] == 'O' and tic_tac_list[9] == 'O' and tic_tac_list[6] == ' ' :
        tic_tac_list[6] = 'O'
    elif tic_tac_list[1] == 'O' and tic_tac_list[9] == 'O' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[3] == 'O' and tic_tac_list[7] == 'O' and tic_tac_list[5] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[7] == 'O' and tic_tac_list[8] == 'O' and tic_tac_list[9] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[1] == 'O' and tic_tac_list[3] == 'O' and tic_tac_list[2] == ' ' :
        tic_tac_list[2] = 'O'
    elif tic_tac_list[4] == 'O' and tic_tac_list[6] == 'O' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[7] == 'O' and tic_tac_list[4] == 'O' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[8] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[2] == ' ' :
        tic_tac_list[2] = 'O'
    elif tic_tac_list[9] == 'O' and tic_tac_list[6] == 'O' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[9] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[7] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[9] == 'O' and tic_tac_list[8] == 'O' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[3] == 'O' and tic_tac_list[2] == 'O' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[6] == 'O' and tic_tac_list[5] == 'O' and tic_tac_list[4] == ' ' :
        tic_tac_list[4] = 'O'
    else : one_is_empty = 1
    #print("smart_pick: one is empty",one_is_empty) 


def block() :
    global one_is_empty
    one_is_empty = 0
    #print("block routine",one_is_empty)   
    if tic_tac_list[1] == 'X' and tic_tac_list[4] == 'X' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[2] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[8] == ' ' :
        tic_tac_list[8] = 'O'
    elif tic_tac_list[3] == 'X' and tic_tac_list[6] == 'X' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[1] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[3] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[7] == 'X' and tic_tac_list[8] == 'X' and tic_tac_list[9] == ' ' :
        tic_tac_list[9] = 'O'
    elif tic_tac_list[1] == 'X' and tic_tac_list[2] == 'X' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[4] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[6] == ' ' :
        tic_tac_list[6] = 'O'
    elif tic_tac_list[1] == 'X' and tic_tac_list[7] == 'X' and tic_tac_list[4] == ' ' :
        tic_tac_list[4] = 'O'
    elif tic_tac_list[2] == 'X' and tic_tac_list[8] == 'X' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[3] == 'X' and tic_tac_list[9] == 'X' and tic_tac_list[6] == ' ' :
        tic_tac_list[6] = 'O'
    elif tic_tac_list[1] == 'X' and tic_tac_list[9] == 'X' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[3] == 'X' and tic_tac_list[7] == 'X' and tic_tac_list[5] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[7] == 'X' and tic_tac_list[8] == 'X' and tic_tac_list[9] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[1] == 'X' and tic_tac_list[3] == 'X' and tic_tac_list[2] == ' ' :
        tic_tac_list[2] = 'O'
    elif tic_tac_list[4] == 'X' and tic_tac_list[6] == 'X' and tic_tac_list[5] == ' ' :
        tic_tac_list[5] = 'O'
    elif tic_tac_list[7] == 'X' and tic_tac_list[4] == 'X' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[8] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[2] == ' ' :
        tic_tac_list[2] = 'O'
    elif tic_tac_list[9] == 'X' and tic_tac_list[6] == 'X' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[9] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[7] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[3] == ' ' :
        tic_tac_list[3] = 'O'
    elif tic_tac_list[9] == 'X' and tic_tac_list[8] == 'X' and tic_tac_list[7] == ' ' :
        tic_tac_list[7] = 'O'
    elif tic_tac_list[3] == 'X' and tic_tac_list[2] == 'X' and tic_tac_list[1] == ' ' :
        tic_tac_list[1] = 'O'
    elif tic_tac_list[6] == 'X' and tic_tac_list[5] == 'X' and tic_tac_list[4] == ' ' :
        tic_tac_list[4] = 'O'
    else : one_is_empty = 1
    #print("block routine",one_is_empty)
        
#makes variable printer print board
def printer() :
    print("     ||     ||  ")
    print('[',tic_tac_list[1],']||[',tic_tac_list[2],']||[',tic_tac_list[3],']')
    print("=====||=====||=====")
    print('[',tic_tac_list[4],']||[',tic_tac_list[5],']||[',tic_tac_list[6],']')
    print("=====||=====||=====")
    print('[',tic_tac_list[7],']||[',tic_tac_list[8],']||[',tic_tac_list[9],']')
    print("     ||     || ")


def computer_picks() :
    global one_is_empty
    
    one_is_empty = 0
    for x in tic_tac_list :
        if x == ' ' :
            one_is_empty = 1

    if not one_is_empty :
        print("it was a draw but we both know the computer had the upper hand")
       
                
    smart_pick()

    if one_is_empty :
        block()

    while one_is_empty :
        #print("random_pick: one_is_empty", one_is_empty)
        random_num = random.randint(1,9)
        if tic_tac_list[random_num] == ' ' :
            tic_tac_list[random_num] = 'O'
            one_is_empty = 0


#prints board
printer()

#while no one wins it takes your input as an intiger,clears previous board,ticktack list mumber selection becomes 'x'
#cont. then the computer picks an O and re-prints the board
while not game_over:
    selection = int(input("It's your turn X.  Enter your Selection between 1 and 9 ...  "))
    os.system('cls')
    #new
    if tic_tac_list[selection] != ' ' :
        print ("YOU DOFUS THAT SQUARE IS OCCUPIED")
        printer()
        continue
    #new
    if selection >= 10 :
        print("YOU DOFUS I SAID 1-9!")
        continue
    tic_tac_list[selection] = 'X'
    #printer()
    check_if_game_over()
    if game_over: printer()  
    if game_over: break
    print('Now the computer will pick an o')
    computer_picks()
    printer()
    check_if_game_over()
    
#you win or comp wins
if game_over == 1 : print ('You Won!!!! Now do something constructive with your life!')
else : print('You are a complete moron.')

#exiting
input('press enter to exit')


#if tic_tac_list[int(temp_counter)] == tic_tac_list[input]() :
    #print("occupied")

#maximum number entered
#need x over ride
#free png editor(alphabet), draw X and O


#if input != int (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) :
#    print(" I SAID 1-9 doofus")



