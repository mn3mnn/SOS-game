''' 
    FCAI-CU  CS112 
    Monaem Tarek
    ID 20210220
    
    * SOS Game *

  - box numbers are start from top-left 
    
    = = = = = = = = = = = =
   |  1  |  2  |  3  |  4  |
   = = = = = = = = = = = =
   |  5  |  6  |  7  |  8  |
   = = = = = = = = = = = =
   |  9  | 10  | 11  | 12  |
   = = = = = = = = = = = =
   | 13  | 14  | 15  | 16  |
   = = = = = = = = = = = =

 - create straight sequence S-O-S among connected squares (either diagonally, horizontally, or
   vertically) to win 1 point and take extra turn. Otherwise turns alternate between players after each move.

    = = = = = = = = = = = =
   |  S  |  O  |  S  |  S  |
   = = = = = = = = = = = =
   |     |     |  O  |  O  |
   = = = = = = = = = = = =
   |     |  S  |     |  S  |
   = = = = = = = = = = = =
   |     |     |     |     |
    = = = = = = = = = = = =

    - Game ends when there are non boxes left 

    '''

# import module to color the output on terminal
import colorama
from colorama import Fore
colorama.init(autoreset=True) 

# set playing box size 
size = int(input("Enter box size - 4 or 5 - :  ")) 

POS = [f"  {x}  " for x in range(10)]   # create list with all box positions
POS.extend([f" {x}  " for x in range(10, size**2 +1 )])


def show_statues():  # print the boxes with the update 
    global size
    if size == 4:
        print(f"""
                        = = = = = = = = = = = = 
                        |{POS[1]}|{POS[2]}|{POS[3]}|{POS[4]}|
                        = = = = = = = = = = = = 
                        |{POS[5]}|{POS[6]}|{POS[7]}|{POS[8]}|
                        = = = = = = = = = = = = 
                        |{POS[9]}|{POS[10]}|{POS[11]}|{POS[12]}|
                        = = = = = = = = = = = = 
                        |{POS[13]}|{POS[14]}|{POS[15]}|{POS[16]}|
                        = = = = = = = = = = = = 
                        """)
        
    elif size == 5:
        print(f"""
                    = = = = = = = = = = = = = = = = 
                    |{POS[1]}|{POS[2]}|{POS[3]}|{POS[4]}|{POS[5]}|
                    = = = = = = = = = = = = = = = = 
                    |{POS[6]}|{POS[7]}|{POS[8]}|{POS[9]}|{POS[10]}|
                    = = = = = = = = = = = = = = = = 
                    |{POS[11]}|{POS[12]}|{POS[13]}|{POS[14]}|{POS[15]}|
                    = = = = = = = = = = = = = = = = 
                    |{POS[16]}|{POS[17]}|{POS[18]}|{POS[19]}|{POS[20]}|
                    = = = = = = = = = = = = = = = = 
                    |{POS[21]}|{POS[22]}|{POS[23]}|{POS[24]}|{POS[25]}|
                    = = = = = = = = = = = = = = = =
                    """)
       

def start_box(size):   # draw the box for the first time
    print("""box numbers are start from top-left 
    
    = = = = = = = = = = = =
   |  1  |  2  |  3  |  4  |
   = = = = = = = = = = = =
   |  5  |  6  |  7  |  8  |
   = = = = = = = = = = = =
   |  9  | 10  | 11  | 12  |
   = = = = = = = = = = = =
   | 13  | 14  | 15  | 16  |
   = = = = = = = = = = = =
        """)    


def show_score(score1, score2):  # show the score
    print(" * " *30)
                                # color the output for each player
    print(f"                     {Fore.GREEN}   player1 {Fore.WHITE}--> {score1}")
    print(f"                     {Fore.YELLOW}   player2 {Fore.WHITE}--> {score2}")
    print(" * " *30)


def player1_input():    # get valid input from player1 and return it 
    validity = False

    while validity is False:

        t1 = input("player1 enter 'S' or 'O' : ").strip()  # take 'S' or 'O' only
        t1 = t1.upper()  

        if t1 == 'S' or t1 == 'O': 
            break

        elif validity is False:
            print("wrong input try again ")

    t1 = Fore.GREEN + t1 # make input color for player1 green      
    return t1  # return colored letter 


def player2_input():     # get valid input from player2 and return it 
    validity = False

    while validity is False:
        t2= input("player2 enter 'S' or 'O' : ").strip() # take 'S' or 'O' only
        t2 = t2.upper()       

        if t2 == 'S' or t2 == 'O':
            break

        elif validity is False:
            print("wrong input try again ")
    
    t2 = Fore.YELLOW + t2  # make input color for player1 yellow
    return t2 


def check_pos(position): # check if the position is empty or not 
    global POS    
    try:    # check if the position is = to the initial value  
            #      "  {box number}  "  with 2 spaces before and after the numbers < 10
            #  and " {box number}  "   with 1 space before and 2 spaces after the numbers >= 10
        if POS[position] == f" {position}  " or POS[position] == f"  {position}  " :
            return True
        else:
            return False
    except:
        return False

    
def postion_input(t): # takes the letter and place it into the POS list 
    global POS

    p = int(input("enter the position : "))
    valid = check_pos(p)  # check if the position is empty or not 

    while valid is False: # if the position is wrong, loop to take a correct pos
        
        print("the box is un available ")
        
        p = int(input("enter the position : "))
        valid = check_pos(p)

    
    # add the input to the positions list and reset the color
    POS.pop(p)  
    POS.insert(p, f"  {t}{Fore.RESET}  ")  

    return p  # return a valid position in POS
    
    
def win_point(pos, player): # check if the input complete the seq
    global size, POS

    column = int(pos % size) # which column we stand on
    points = 0 
    pos = int(pos)

    # set the borders of the box
    if size == 4: 
        borders = [1,2,3,4,5,9,13,14,15,16,12,8] 

        # borders without the corners
        north_border = [2, 3]
        west_border = [5, 9]
        south_border = [14, 15]
        east_border = [8, 12]

    elif size == 5:
        borders = [1,2,3,4,5,6,11,16,21,22,23,24,25,20,15,10] 

        # borders without the corners
        north_border = [2, 3, 4]
        west_border = [6, 11, 16]
        south_border = [22, 23, 24]
        east_border = [10 , 15, 20]

    # create var with the colored letter to check the seq is complete sos with the others in the POS list
    if player == 1:                   
        the_s_letter = '  \x1b[32mS\x1b[39m  '  # letter S green
        the_o_letter = '  \x1b[32mO\x1b[39m  '  # letter O green

    if player == 2:
        the_s_letter = '  \x1b[33mS\x1b[39m  '  # letter S yellow
        the_o_letter = '  \x1b[33mO\x1b[39m  '  # letter S yellow
    
    
    def check_the_north(): # check two boxes to the north 
        nonlocal points, pos 
        try:
            if POS[pos-size] == the_o_letter and POS[pos-2*size] == the_s_letter: 
                points += 1
        except:
            pass


    def check_the_east(): # check two boxes to the east
        nonlocal points, pos
        try:
            if POS[pos+1] == the_o_letter and POS[pos+2] == the_s_letter: 
                points += 1
        except:
            pass


    def check_the_south(): # check two boxes to the south 
        nonlocal points, pos
        try:
            if POS[pos+size] == the_o_letter and POS[pos+2*size] == the_s_letter: 
                points += 1
        except:
            pass


    def check_the_west(): # check two boxes to the west
        nonlocal points, pos
        try:
            if POS[pos - 1] == the_o_letter and POS[pos - 2] == the_s_letter:  
                points += 1
        except:
            pass
        


    def check_the_south_east(): # check two boxes to the south-east
        nonlocal points, pos
        try:
            if POS[pos+ (size + 1)] == the_o_letter and POS[pos+ 2*(size + 1)] == the_s_letter:  
                points += 1
        except:
            pass


    def check_the_south_west(): # check two boxes to the south-west
        nonlocal points, pos
        try:
            if POS[pos+ (size - 1)] == the_o_letter and POS[pos+ 2*(size - 1)] == the_s_letter:  
                points += 1
        except:
            pass


    def check_the_north_east(): # check two boxes to the north-east
        nonlocal points, pos
        try:
            if POS[pos-(size - 1)] == the_o_letter and POS[(pos- 2*(size - 1))] == the_s_letter: 
                points += 1
        except:
            pass


    def check_the_north_west(): # check two boxes to the north-west
        nonlocal points, pos
        try:
            if POS[pos - (size + 1)] == the_o_letter and POS[pos -2*(size + 1)] == the_s_letter:  
                points += 1
        except:
                pass


    #   we check all posible directions if we input 's' and it completes the seq
    if POS[pos] == the_s_letter:
        #    if the box is in column 1 or 2 check the east, south and north directions
        if column == 1 or column == 2:
            check_the_east()

            check_the_south()

            check_the_north()
                    
            check_the_south_east()
            
            check_the_north_east()
            
        #   if the box is in column 3 or 4 check the west, south and north directions
        elif size == 4 and column == 3 or column == 0 : 
            
            check_the_south_west()
            
            check_the_north_west()

            check_the_west()

            check_the_north()

            check_the_south()

        #  if the box is in column 4 or 5 check the west, south and north directions
        elif size == 5 and column == 4 or column == 0 :
            
            check_the_south_west()
            
            check_the_north_west()

            check_the_west()

            check_the_north()

            check_the_south()

        #   if the box is in column 3 in 5x5 box check all directions
        elif column == 3 and size == 5 : 
            check_the_south_west()
            
            check_the_north_west()

            check_the_west()

            check_the_north()

            check_the_south()

            check_the_south_east()
            
            check_the_north_east()

            check_the_east()

    # check if we input 'o' and completed the seq 
    if POS[pos] == the_o_letter:
        if pos not in borders:  # if we input 'o' and pos not in the borders box we check all directions

            if POS[pos+1] == the_s_letter and POS[pos-1] == the_s_letter:
                points += 1

            if POS[pos- (size - 1)] == the_s_letter and POS[pos+ (size - 1)] == the_s_letter:
                points += 1

            if POS[pos+size] == the_s_letter and POS[pos-size] == the_s_letter:
                points += 1

            if POS[pos+ (size + 1)] == the_s_letter and POS[pos- (size + 1)] == the_s_letter:
                points += 1
        
        elif pos in north_border or pos in south_border: # if we input 'o' in the north or south border check only left and right
            if POS[pos+1] == the_s_letter and POS[pos-1] == the_s_letter:
                points += 1

        elif pos in west_border or pos in east_border: # if we input 'o' in the west or east border check only up and down
            if POS[pos+size] == the_s_letter and POS[pos-size] == the_s_letter:
                points += 1
                    
    return points


def check_winner(score1, score2): # check if the game is over and if it's over print the winner
    global POS
    game_over = True

    if score1 == score2:
        winner = " DRAW "    

    elif score1 > score2:
        winner = f" PLAYER 1 wins"
    
    elif score2 > score1:
        winner = f" PLAYER 2 wins"

    for box in range(1, len(POS)):

        if POS[box] == f"  {box}  " or POS[box] == f" {box}  ": # if there are available boxes return false
            game_over = False
            break

    if game_over:
        print("#"* 60)
        print(" GAME END ! \n")
        print(winner, "\n")
        print("#"* 60)
        return True
    
    return False


def play_sos(): 
    score1 = 0
    score2 = 0
    
    # print the box and the score set to 0
    show_statues()
    show_score(score1, score2) 

    win = False
    while win is False: # playing the game

        while win is False:  #  player1 turn 
            
            # take input
            t1 = player1_input() 
           
            # take position
            pos1 = postion_input(t1)
            
            # check if SOS completed or not
            points1 = win_point(pos1, 1)
            
            # increase the score with the points player has won
            score1 += points1
            
            # show the score and update the screen
            show_statues()
            show_score(score1, score2)
            
            if points1 < 1:  # if the player hasn't get any points change turns
                win = check_winner(score1, score2)
                break

            elif points1 >= 1 : # update the score 
                print(f" YOU GET {points1} POINTS ! Take another turn ")
                win = check_winner(score1, score2)  # return true if there're no boxes left


        while win is False:   #  player2 turn
            # take input
            t2 = player2_input()

            # take position
            pos2 = postion_input(t2)
            
            # check if SOS completed or not
            points2 = win_point(pos2, 2)

            # increase the score with the points won
            score2 += points2
            
             # show the score and update the screen
            show_statues()
            show_score(score1, score2)
            
            if points2 < 1:  # if the player hasn't get any points change turns
                win = check_winner(score1, score2)
                break

            elif points2 >= 1 : # update the score
                print(f" YOU GET {points2} POINTS ! Take another turn ")
                win = check_winner(score1, score2)  # return true if there're no boxes left

       
play_sos()
