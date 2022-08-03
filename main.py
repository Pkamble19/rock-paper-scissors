import random as ra
SCORE_COM=0
SCORE_USER=0
def user_won():
    global SCORE_USER
    global SCORE_COM
    SCORE_USER+=1
    SCORE_COM+= 0
def com_win():
    global SCORE_USER
    global SCORE_COM
    SCORE_USER+= 0
    SCORE_COM+= 1
def tie():
    global SCORE_USER
    global SCORE_COM
    SCORE_USER+=1
    SCORE_COM+=1

def choice2():
    user_input2=input("Entre YES to Coninue EXIT for Exit ")
    user_input2=user_input2.upper()
    if user_input2 == "YES":
        computer_setting()
    else:
        print("BYE!!!!")
        print("here is your score Computer Score= ",SCORE_COM,"YOUR SCORE= ",SCORE_USER)

def computer_setting():
    com= ["ROCK","PAPER","SCISSOR"]
    com_ra=ra.choice(com)
    print("ENTRE CHOICE NUMBER \n ROCK=1 \n PAPER=2 \n SCISSOR=3 \n")
    user_input=int(input("Entre Your Choice"))
    if user_input==1:
        answer="ROCK"
    elif user_input==2:
        answer= "PAPER"
    elif user_input == 3:
        answer="SCISSOR"
    else:
        print("please Entre a Correct Input")
        computer_setting()
    print("COMPUTER SELECT  '%s'  AND YOU SELECT  '%s' "%(com_ra,answer))

    if com_ra == "ROCK":
        if answer == "SCISSOR":
            print( "You Loose!!!!!")
            com_win()
        if answer == "ROCK":
            print("OH NO IT'S TIE TRY AGAIN")
            tie()
        if answer == "PAPER":
            print("YOU WON!!!!!!!!")
            user_won()

    if com_ra == "PAPER":
        if answer == "SCISSOR":
            print( "You WON!!!!!")
            user_won()
        if answer == "ROCK":
            print("YOU LOOSE!!!!")
            com_win()
        if answer == "PAPER":
            print("OH NO IT'S TIE TRY AGAIN")
            tie()

    if com_ra == "SCISSOR":
        if answer == "SCISSOR":
            print( "OH NO IT'S TIE TRY AGAIN")
            tie()
        if answer == "ROCK":
            print("YOU LOOSE!!!!")
            com_win()
        if answer == "PAPER":
            print("YOU WON!!!!!!!!")
            user_won()
    choice2()

if __name__ == "__main__":

    print("_____________WELCOME TO ROCK,PAPER,SCISSOR____________")
    print()
    play=input("Entre 'PLAY' to start === ")
    play=play.upper()
    if play=="PLAY":
        computer_setting()



